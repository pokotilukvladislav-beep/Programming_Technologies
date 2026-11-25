from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Pawnshop Auction Microservices")

# Імітація бази даних
auction_items = {}
bids_history = {}

# Моделі даних
class Item(BaseModel):
    item_id: str
    name: str
    start_price: float

class Bid(BaseModel):
    item_id: str
    bid_amount: float

# Мікросервіс 1: Управління лотами
@app.post("/items/")
def create_item(item: Item):
    if item.item_id in auction_items:
        raise HTTPException(status_code=400, detail="Лот з таким ID вже існує на аукціоні.")
    
    auction_items[item.item_id] = {
        "name": item.name,
        "current_bid": item.start_price
    }
    bids_history[item.item_id] = []
    return {"status": "item_created", "item": auction_items[item.item_id]}

# Мікросервіс 2: Управління ставками
@app.post("/bids/")
def place_bid(bid: Bid):
    if bid.item_id not in auction_items:
        # Виключна ситуація: лот не знайдено
        raise HTTPException(status_code=404, detail="Лот не знайдено.")
    
    item = auction_items[bid.item_id]
    
    if bid.bid_amount <= item["current_bid"]:
        # Негативний сценарій: ставка менша або рівна поточній
        raise HTTPException(status_code=400, detail="Ставка має бути більшою за поточну ціну.")
    
    item["current_bid"] = bid.bid_amount
    bids_history[bid.item_id].append(bid.bid_amount)
    return {"status": "bid_accepted", "current_bid": bid.bid_amount}

@app.get("/")
def read_root():
    return {"service": "Pawnshop Auction Microservices", "status": "running"}
