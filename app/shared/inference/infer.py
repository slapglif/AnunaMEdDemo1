import re

from pyexpat import model

from app.shared.inference.model import tokenizer


def process_model_output(response):
    return response.split('[/INST]')[1].strip()

def query_model(prompt, new_tokens=500):
    input_ids = tokenizer.encode(prompt, return_tensors='pt').to('cuda')
    generated = model.generate(input_ids=input_ids, max_new_tokens=new_tokens)
    output_text = tokenizer.decode(generated[0], skip_special_tokens=True)
    return process_model_output(output_text)

def parse_diagnosis_text(diagnosis_text):
    diagnosis_match = re.search(r"Diagnosis:\s*([\w ]+)", diagnosis_text)
    score_match = re.search(r"Score:\s*([\d/]+)/100", diagnosis_text)
    #follow_up_questions_match = re.search(r"Follow up questions:(.*?)$", diagnosis_text, re.DOTALL)

    diagnosis = diagnosis_match[1] if diagnosis_match else "Diagnosis not found"
    score = score_match[1] if score_match else "Score not found"

    # if follow_up_questions_match:
    #     follow_up_questions = follow_up_questions_match.group(1).strip()
    #     follow_up_questions_list = re.findall(r"\d+\.\s*(.*?)(?=\d+\.|$)", follow_up_questions, re.DOTALL)
    # else:
    #     follow_up_questions_list = []

    print(f"Captured values: Diagnosis: {diagnosis}, Score: {score}")
    # print("Follow up questions:")
    # for i, question in enumerate(follow_up_questions_list, start=1):
    #   self.potential_question_history.append(question.strip())
    #   print(f"{i}. {question.strip()}")

    return f"Diagnosis: {diagnosis}, Confidence Score: {int(score)}" #, follow_up_questions_list

def product_recommender(input_text):
    product_recommendation_prompt = f"""<<SYS>>You are an AI assistant tasked with recommending natural products to patients. Given information on the patient, recommend two products that they could try <</SYS>>
    [INST]
    Patient information: {input_text}
    Respond to the patient information with two product recommendations and why it will help:
    Recommended products:
    1. [Product 1]
    2. [Product 2]
    [/INST]"""

    return query_model(product_recommendation_prompt)

def wellness_score(input_text):
    diagnosis_prompt = f"""<<SYS>> You are an AI assistant specializing in diagnosing a patient's medical condition. You will respond in a very succinct manner. Given the Patient Information, your job is to:
      1. Provide a possible diagnosis for patient's issue
      2. For the diagnosis, provide a confidence score on a scale of 1 to 100 with 100 being fully confident on the diagnosis with 1 being completely guessing.<</SYS>>
    [INST]
    Patient information: {input_text}
    Respond to the patient information with the Diagnosis and a Confidence Score in the following format:
    Diagnosis: [Diagnosis]
    Confidence Score: [Score]/100
    [/INST]"""

    diagnosis_text = query_model(diagnosis_prompt)

    return parse_diagnosis_text(diagnosis_text)

tools = [
    Tool(
        name = 'Get Wellness Intent Score',
        func = wellness_score,
        description="Useful for when you need to get a diagnosis of the patient's issue and a confidence score. The input to this tool requires a full summary of the patient and their symptoms."
    ),
    Tool(
        name = 'Get Product Recommendation',
        func = product_recommender,
        description='Useful for when you need to get natural products to recommend to the patient. The input to this tool requires a full summary of the patient and their symptoms including their diagnosis'
    )
]