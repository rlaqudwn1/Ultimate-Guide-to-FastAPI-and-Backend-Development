from fastapi import FastAPI, HTTPException, status
from typing import Any

app = FastAPI()

# 목업 데이터
shipments = {
    12701: {"weight": 0.6, "content": "glassware", "status": "placed"},
    12702: {"weight": 2.3, "content": "books", "status": "shipped"},
}

@app.get("/shipment/{field}")
def get_shipment_field(field: str, id: int) -> Any:
    # 1. ID 존재 여부 확인
    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"ID {id}를 찾을 수 없습니다."
        )
    
    # 2. 해당 데이터 내에 요청한 필드(field)가 있는지 확인
    shipment = shipments[id]
    if field not in shipment:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"해당 배송 정보에 '{field}' 항목이 없습니다. (사용 가능 필드: {list(shipment.keys())})"
        )
    
    return {field: shipment[field]}
