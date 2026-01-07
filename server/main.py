from fastapi import FastAPI
from routers.analyze import router
from utils.helpers import parse_json_file 
from dotenv import load_dotenv
from services.gemini_service import analyze_ingredients

app = FastAPI()
app.include_router(router)


if __name__ == "__main__":
    # main()
    import uvicorn
    load_dotenv()
    uvicorn.run(app, host="0.0.0.0", port=8000)
