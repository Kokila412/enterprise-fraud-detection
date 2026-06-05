from pydantic import BaseModel, Field

class TransactionInput(BaseModel):
    sender_upi_id: str = Field(..., min_length=3)
    receiver_upi_id: str = Field(..., min_length=3)
    amount: float = Field(..., gt=0)