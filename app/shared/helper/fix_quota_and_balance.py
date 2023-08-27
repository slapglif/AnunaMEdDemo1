from app.api.agent.models import Agent
from app.api.credit.models import Balance, Quota


for agent in Agent.where():
    if agent.quota:
        continue
    else:
        Quota.create(agentId=agent.id, balance=0)
    for user in agent.users:
        if user.balance.amount:
            continue
        else:
            Balance.create(ownerId=user.id, balance=0)
