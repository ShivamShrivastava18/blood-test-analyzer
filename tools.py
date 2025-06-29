from crewai.tools import BaseTool
from langchain_community.document_loaders import PyMuPDFLoader  # ✅ replace PDFLoader
from crewai_tools import SerperDevTool

# ✅ Create Search Tool (can be passed directly to agents)
search_tool = SerperDevTool()


# ✅ Blood Test Report Tool
class BloodTestReportTool(BaseTool):
    name: str = "Blood Test Report Tool"
    description: str = "Reads and parses blood test PDF reports into clean text format."

    def _run(self, path: str):
        docs = PyMuPDFLoader(file_path=path).load()

        full_report = ""
        for data in docs:
            content = data.page_content

            # Remove double newlines and clean up whitespace
            while "\n\n" in content:
                content = content.replace("\n\n", "\n")
                
            full_report += content + "\n"
        
        return full_report


# ✅ Nutrition Tool
class NutritionTool(BaseTool):
    name: str = "Nutrition Tool"
    description: str = "Analyzes a blood report and gives nutritional advice."

    def _run(self, blood_report_data: str):
        # Simple whitespace cleanup
        processed_data = blood_report_data.replace("  ", " ")
        
        # TODO: Implement actual analysis
        return "Nutrition analysis functionality to be implemented."


# ✅ Exercise Tool
class ExerciseTool(BaseTool):
    name: str = "Exercise Tool"
    description: str = "Analyzes blood report and returns a personalized exercise plan."

    def _run(self, blood_report_data: str):
        # TODO: Implement actual logic
        return "Exercise planning functionality to be implemented."
