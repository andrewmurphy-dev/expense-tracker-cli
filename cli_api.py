from fastapi import FastAPI , HTTPException 
from pydantic import BaseModel, Field
from storage import load_expenses, save_expenses  


app = FastAPI

#make base model ! 

class correctstructure(BaseModel):
    name: str = Field(Min_length=1)
    price: int = Field(gt=0)


#we need to have seed data ! 
#you actually do not need to add seed data ! 
#because you can save it in storage ! 
#remmever json.dump

expenses = {
    "coffee": 300,
    "train": 220,
    "food": 800
}





@app.get("/expenses")
def get_expenses():
    expenses = load_expenses()
    return expenses 




#add a new expenses !

@app.post("/expenses")
def add_expenses(expense: correctstructure):
    expenses = load_expenses() 

    expenses[expense.name] = expense.price

    save_expenses(expenses)

    return  {
        "message": "expense added",
        "expenses": expenses 

    }



@app.delete("/expenses/{expense_name}")
def delete_expense(expense_name: str):
    expense_name = expense_name.lower().strip()
    expenses = load_expenses()

    if expense_name not in expenses:
        raise HTTPException(status_code=404, detail="Expense not found")
    
    del expenses[expense_name]

    save_expenses(expenses)

    return {
        "message": "Expense deleted",
        "expenses": expenses
    }




#just confused where is this response going 
#the user will sen da request with expense data ! 
#what i find confusing is when to use / and {} in the parameter 








