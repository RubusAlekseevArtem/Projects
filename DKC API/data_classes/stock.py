from dataclasses import dataclass
from typing import List


@dataclass
class Receipt:
    date: int | None = None
    amount: int | None = None


@dataclass
class Warehouse:
    code: str | None = None
    amount: int | None = None
    receipts: List[Receipt] | None = None


@dataclass
class MaterialsStock:
    id: int | None = None
    status: int | None = None
    code: str | None = None
    warehouses: List[Warehouse] | None = None
    avg_delivery: dict | None = None


@dataclass
class Stock:
    create: int | None = None
    materials: List[MaterialsStock] | None = None


"""
https://api.dkc.ru/v1/catalog/material/stock?code=4400003
{
  "create": 1674472206,
  "materials": [
    {
      "id": 41542,
      "status": 1,
      "code": "4400003",
      "warehouse": [
        {
          "code": "1100",
          "amount": 0,
          "receipt": [
            {
              "date": 1677358800,
              "amount": 1053
            },
            {
              "date": 1678914000,
              "amount": 15000
            }
          ]
        },
        {
          "code": "1200",
          "amount": 0,
          "receipt": [
            {
              "date": 1678914000,
              "amount": 1258
            }
          ]
        },
        {
          "code": "1600",
          "amount": 908,
          "receipt": []
        }
      ],
      "avg_delivery": {
        "1100": 100,
        "1200": 119,
        "1600": 134
      }
    }
  ]
}
"""
