# from fastapi import FastAPI, File, UploadFile, Form, HTTPException
# import os, uuid, shutil

# from agents import agents
# from task import tasks
# from crewai import Crew, Process

# app = FastAPI(title="Blood Test Report Analyser")

# @app.get("/")
# def root():
#     return {"message": "Blood Test Report Analyser API is running"}

# @app.post("/analyze")
# async def analyze_blood_report(
#     file: UploadFile = File(...),
#     query: str = Form(default="Summarise my Blood Test Report")
# ):
#     file_id = str(uuid.uuid4())
#     file_path = f"data/blood_test_report_{file_id}.pdf"

#     try:
#         os.makedirs("data", exist_ok=True)
#         with open(file_path, "wb") as f:
#             shutil.copyfileobj(file.file, f)

#         if not query.strip():
#             query = "Summarise my Blood Test Report"

#         crew = Crew(
#             agents=agents,
#             tasks=tasks,
#             process=Process.sequential
#         )

#         result = crew.kickoff(
#             inputs={
#                 "query": query.strip(),
#                 "file_path": file_path
#             }
#         )

#         return {
#             "status": "success",
#             "query": query,
#             "analysis": str(result),
#             "file_processed": file.filename
#         }

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

#     finally:
#         if os.path.exists(file_path):
#             try:
#                 os.remove(file_path)
#             except:
#                 pass
from fastapi import FastAPI, File, UploadFile, Form, HTTPException
import os, uuid, shutil
from datetime import datetime

from agents import agents
from task import tasks
from crewai import Crew, Process
from database import database
from models import results

app = FastAPI(title="Blood Test Report Analyser")

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/")
def root():
    return {"message": "Blood Test Report Analyser API is running"}

@app.post("/analyze")
async def analyze_blood_report(
    file: UploadFile = File(...),
    query: str = Form(default="Summarise my Blood Test Report"),
    user_id: str = Form(default="anonymous")  # optional
):
    file_id = str(uuid.uuid4())
    file_path = f"data/blood_test_report_{file_id}.pdf"

    try:
        os.makedirs("data", exist_ok=True)
        with open(file_path, "wb") as f:
            shutil.copyfileobj(file.file, f)

        if not query.strip():
            query = "Summarise my Blood Test Report"

        crew = Crew(
            agents=agents,
            tasks=tasks,
            process=Process.sequential
        )

        result = crew.kickoff(inputs={"query": query.strip(), "file_path": file_path})

        # ✅ Store result in database
        await database.execute(results.insert().values(
            user_id=user_id,
            query=query,
            file_name=file.filename,
            analysis=str(result),
            timestamp=datetime.utcnow()
        ))

        return {
            "status": "success",
            "query": query,
            "analysis": str(result),
            "file_processed": file.filename
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

    finally:
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
            except:
                pass
