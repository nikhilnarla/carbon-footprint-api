class Config:
    """Set Flask configuration vars from .env file."""

    # Database
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://sHpRfE2dLA:42boy0LUUT@remotemysql.com:3306/sHpRfE2dLA'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
