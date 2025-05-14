import logging
from typing import TypedDict
from IPython.display import Image, display
from langgraph.graph import StateGraph, END
from langchain_core.runnables import RunnableLambda
from llm_client import ask_gemini
from llm_client import ask_gemini_pro_preview
from PIL import Image as PILImage
from IPython.display import Image as DisplayImage, display
import io
import io
# Gemini LLM çağrısı yapan yardımcı fonksiyon

# Setup
logging.basicConfig(level=logging.INFO)

# Agent durumu (gelişerek büyür)
class CVAgentState(TypedDict):
    job_posting: str
    cv_text: str
    skills_analysis: str
    experience_analysis: str
    project_analysis: str
    final_summary: str

# Step 1 – Yetenek analizi
def analyze_skills_node(state: CVAgentState) -> CVAgentState:
    prompt = f"""
Aşağıda bir iş ilanı ve adayın CV'si bulunmaktadır. CV'deki yetenekleri analiz et:

İş İlanı:
{state['job_posting']}

CV:
{state['cv_text']}

Yapılacaklar:
- İlandaki istenen yetenekleri bul ve eşleşenleri yaz.
- Eksik olanları da belirt.
- 0–40 arası puan ver.

Yanıt formatı:
Eşleşen Yetenekler: [...]
Eksik Yetenekler: [...]
Puan: int (0–40)
"""
    result = ask_gemini(prompt).strip()
    return {**state, "skills_analysis": result}

# Step 2 – Tecrübe analizi
def analyze_experience_node(state: CVAgentState) -> CVAgentState:
    prompt = f"""
Adayın tecrübesini değerlendir.

İş İlanı:
{state['job_posting']}

CV:
{state['cv_text']}

Yapılacaklar:
- Kaç yıl deneyimi olduğunu tespit et.
- Alan uygunluğu nedir?
- 0–35 arası puan ver.

Yanıt formatı:
Tecrübe Yılı: X
Uygunluk: low|medium|high
Tecrübe Puan: int (0–35)
"""
    result = ask_gemini(prompt).strip()
    return {**state, "experience_analysis": result}

# Step 3 – Proje analizi
def analyze_projects_node(state: CVAgentState) -> CVAgentState:
    prompt = f"""
Adayın projelerini değerlendir.

İş İlanı:
{state['job_posting']}

CV:
{state['cv_text']}

Yapılacaklar:
- CV’deki projeleri belirle
- İlanla ne kadar uyumlu olduklarını değerlendir
- 0–25 arası puan ver

Yanıt formatı:
Related Projects: [...]
Project Score: int (0–25)
"""
    result = ask_gemini(prompt).strip()
    return {**state, "project_analysis": result}

# Step 4 – Final özet ve genel değerlendirme
def summarize_all_node(state: CVAgentState) -> CVAgentState:
    prompt = f"""
Adayın yetenek, tecrübe ve proje analizleri aşağıdadır. Buna göre 100 üzerinden toplam puanı hesapla ve 200–300 karakterlik kısa bir özet üret.

Yetenekler:
{state['skills_analysis']}

Tecrübe:
{state['experience_analysis']}

Projeler:
{state['project_analysis']}

Yanıt formatı:
Total Score: int (0–100)
Final Summary: "...200–300 karakterlik yorum..."
"""
    result = ask_gemini(prompt).strip()
    return {**state, "final_summary": result}

# LangGraph tanımı
graph_builder = StateGraph(CVAgentState)
graph_builder.set_entry_point("analyze_skills")

graph_builder.add_node("analyze_skills", analyze_skills_node)
graph_builder.add_node("analyze_experience", analyze_experience_node)
graph_builder.add_node("analyze_projects", analyze_projects_node)
graph_builder.add_node("summarize_all", summarize_all_node)

graph_builder.add_edge("analyze_skills", "analyze_experience")
graph_builder.add_edge("analyze_experience", "analyze_projects")
graph_builder.add_edge("analyze_projects", "summarize_all")
graph_builder.add_edge("summarize_all", END)

graph = graph_builder.compile()

# Dışa açık fonksiyon
def run_cv_pipeline(job_posting: str, cv_text: str):
    #png_data = graph.get_graph().draw_mermaid_png()

    # Görseli göstermek istersen:
    """display(DisplayImage(png_data))
    image = PILImage.open(io.BytesIO(png_data))
    image.save("cv_pipeline_graph.png")
    print("✅ Graph başarıyla kaydedildi: cv_pipeline_graph.png")"""
    inputs: CVAgentState = {
        "job_posting": job_posting,
        "cv_text": cv_text,
        "skills_analysis": "",
        "experience_analysis": "",
        "project_analysis": "",
        "final_summary": ""
    }
    return graph.invoke(inputs)
