from ocr_reader import extract_text_from_pdf
from langgraph_pipeline import run_cv_pipeline


def main():
    # 1. İş ilanı (metin olarak girilebilir ya da dosyadan okunabilir)
    job_posting = """
    Globally recognized for its innovation and investment in groundbreaking technologies, Nurol Teknoloji is committed to pushing the boundaries of success. To support our Smart Factory / Industry 4.0 initiatives, we are seeking a Software Development Engineer to join our Digital Technologies Team.



The position is based in Ankara and requires on-site work at Nurol Teknoloji’s Gölbaşı facility.



Qualifications:



Bachelor’s degree in Computer Engineering, Software Engineering, or Electrical and Electronics Engineering.
Minimum 5 years of experience in Java development and application design.
At least 3 years of hands-on experience with Spring Framework (Spring Boot, Spring MVC, Spring Core).
Solid knowledge of RDBMS and NoSQL technologies.
Familiarity with queue management, microservices architecture, and containerization concepts.
Interest in cloud technologies and their implementation.
Strong problem-solving skills, analytical thinking, and teamwork capabilities.


Job Responsibilities:



Develop and manage digital transformation projects aligned with company objectives and technical requirements.
Contribute to the development of new digital products and ensure their efficient execution.
Analyze existing applications, enhance system performance, and implement scalable solutions.
Stay updated with emerging IT technologies to automate and modernize existing systems.
    """

    # 2. CV PDF dosyasını OCR ile oku
    cv_path = "yakut_eren_Cv.pdf"  # kendi dosya yolunu gir
    print("📄 CV PDF dosyası OCR ile okunuyor...")
    cv_text = extract_text_from_pdf(cv_path)

    # 3. LangGraph pipeline’ını çalıştır
    print("🧠 CV değerlendirme başlatılıyor...\n")
    result = run_cv_pipeline(job_posting, cv_text)

    # 4. Sonuçları yazdır
    print("\n--- Yetenek Analizi ---")
    print(result["skills_analysis"])

    print("\n--- Tecrübe Analizi ---")
    print(result["experience_analysis"])

    print("\n--- Proje Analizi ---")
    print(result["project_analysis"])

    print("\n✅ Genel Değerlendirme ve Özet:")
    print(result["final_summary"])


if __name__ == "__main__":

    main()
