from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

app = FastAPI(
    title="Your API Title",
    description="Your API Description",
    version="0.01"  
)



# Root route redirects to documentation
@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")  # Redirect to the Swagger UI docs

# Example route to show the API is working
@app.get("/ping")
def ping():
    return {"message": "PayLite API is running!"}


# Example route to show the API is working
@app.get("/vassist")
def Vassist():
    return {"message": "PayLite virtual assistant is running!"}