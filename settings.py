import os

from dotenv import load_dotenv


load_dotenv()
base_dir = f"{os.path.dirname(os.path.abspath(__file__))}"

class Config:
    postgres_connection: str = os.getenv("POSTGRES_CONNECTION", "")
    fastapi_host: str = os.getenv("FASTAPI_HOST", "0.0.0.0")
    fastapi_port: int = int(os.getenv("FASTAPI_PORT", 8000))
    fastapi_key: str = os.getenv("FASTAPI_KEY", "")
    salt: str = os.getenv("SALT", "")
    jwt_algo: str = os.getenv("JWT_ALGO")
    admin_key: str = os.getenv("ADMIN_KEY")
    agent_key: str = os.getenv("AGENT_KEY")
    mailgun_key: str = os.getenv("MAILGUN_KEY", "")
    mailgun_host: str = os.getenv("MAILGUN_HOST", "")
    twilio_sid: str = os.getenv("TWILIO_SID", "")
    twilio_token: str = os.getenv("TWILIO_TOKEN", "")
    twilio_phone: str = os.getenv("TWILIO_PHONE", "")
    redis_host: str = os.getenv("REDIS_HOST", "")
    auth0_client_id: str = os.getenv("AUTH0_CLIENT_ID", "")
    auth0_client_secret: str = os.getenv("AUTH0_CLIENT_SECRET", "")
    auth0_domain: str = os.getenv("AUTH0_DOMAIN", "")
    aws_access_key_id: str = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_access_key: str = os.getenv("AWS_SECRET_ACCESS_KEY")
    s3_image_bucket: str = os.getenv("S3_IMAGE_BUCKET")
    s3_video_bucket: str = os.getenv("S3_VIDEO_BUCKET")
    broker_url: str = os.getenv("BROKER_URL", "")
    celery_database: str = os.getenv("CELERY_DATABASE", "")
    workers: int = int(os.getenv("WORKERS", 1))
    reload: bool = os.getenv("RELOAD", False)
    sentry_ingestion_url: str = os.getenv("SENTRY_INGESTION_URL", "")
    sentry_environment: str = os.getenv("SENTRY_ENVIRONMENT", "local")
    meilisearch_url: str = os.getenv("MEILISEARCH_URL", "")
    meili_admin_key: str = os.getenv("MEILI_ADMIN_KEY", "")
    meili_query_key: str = os.getenv("MEILI_QUERY_KEY", "")
    debug_log = os.getenv("DEBUG_LOG", "")
    info_log = os.getenv("INFO_LOG", "")
    warning_log = os.getenv("WARNING_LOG", "")
    error_log = os.getenv("ERROR_LOG", "")
    critical_log = os.getenv("CRITICAL_LOG", "")
    jira_org = os.getenv(
        "JIRA_ORG",
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5oYnRhZHB3d2RoeXpydXdtaHVzIiwicm9sZSI6ImFub24iLCJpYXQiOjE2Nzk0ODQwNDIsImV4cCI6MTk5NTA2MDA0Mn0.-B7sQ1l-XFWwi2D-Lnbqu9W9dOrNAHMw9zI2cAD2dAw",
    )
    jira_user = os.getenv(
        "JIRA_USER",
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5oYnRhZHB3d2RoeXpydXdtaHVzIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY3OTQ4NDA0MiwiZXhwIjoxOTk1MDYwMDQyfQ.mJHxYlM9KaXUFslD4iEw8cpOeihJWgzMzFhE1FKecJA",
    )
    jira_key = os.getenv("JIRA_KEY", "ty66G3lFl6VmnPQh")
    otp_base = os.getenv("OTP_BASE", "LOG6DLW7LGOGTDLT4A7W4G4K5UFX37IN")
    otp_reset_time = os.getenv("OTP_RESET_TIME", "minutes=3")
    rtp_pool_max: float = os.getenv("RTP_POOL_MAX", 0.85)
    rtp_user_min: int = os.getenv("RTP_USER_MIN", 0)
