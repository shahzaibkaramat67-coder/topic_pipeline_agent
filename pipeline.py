from outliner import outline_create
from writter import writter
from editer import Editer
from analyzer import Analyzer
import json
from json_hendler import Json_hendler


async def pipeline(topic):

    print("\n" + "=" * 60)
    print("🚀 PIPELINE STARTED")
    print("=" * 60)
    print(f"[INPUT] Topic: {topic}")

    # =========================================================
    # OUTLINE
    # =========================================================
    print("\n[OUTLINE] Starting outline creation...")

    outline = await outline_create(topic)

    print("[OUTLINE] Outline created successfully.")
    print(f"[OUTLINE] Type: {type(outline)}")
    print(f"[OUTLINE] Length: {len(outline)}")

    # ---------------- OUTLINE ANALYSIS ----------------
    print("\n[OUTLINE ANALYZER] Analyzing outline...")

    outline_analyzer = await Analyzer(outline)

    print("[OUTLINE ANALYZER] Raw response:")
    print(outline_analyzer)

    analysis = json.loads(outline_analyzer)
    # json_result = json.loads(outline_analyzer)
    # analysis = Json_hendler(json_result)

    print(f"[OUTLINE ANALYZER] Approved: {analysis['Approved']}")
    print(f"[OUTLINE ANALYZER] Feedback: {analysis.get('Feedback', '')}")

    # ---------------- OUTLINE RETRY LOOP ----------------
    while not analysis["Approved"]:

        print("\n[OUTLINE] ❌ Outline rejected.")
        print("[OUTLINE] 🔄 Creating improved outline...")

        outline = await outline_create(analysis["Feedback"])

        print("[OUTLINE] Improved outline created.")

        print("[OUTLINE ANALYZER] Re-analyzing outline...")

        outline_analyzer = await Analyzer(outline)
        analysis = json.loads(outline_analyzer)
        # json_result = json.loads(outline_analyzer)
        # analysis = Json_hendler(json_result)

        print(f"[OUTLINE ANALYZER] Approved: {analysis['Approved']}")
        print(f"[OUTLINE ANALYZER] Feedback: {analysis.get('Feedback', '')}")

    print("\n[OUTLINE] ✅ Outline approved.")

    # =========================================================
    # ARTICLE WRITING
    # =========================================================
    print("\n[WRITER] Starting article writing...")

    article = await writter(outline)

    print("[WRITER] Article written successfully.")
    print(f"[WRITER] Type: {type(article)}")
    print(f"[WRITER] Length: {len(article)}")

    # ---------------- ARTICLE ANALYSIS ----------------
    print("\n[ARTICLE ANALYZER] Analyzing article...")

    article_analysis = await Analyzer(article)

    print("[ARTICLE ANALYZER] Raw response:")
    print(article_analysis)

    analysis = json.loads(article_analysis)

    print(f"[ARTICLE ANALYZER] Approved: {analysis['Approved']}")
    print(f"[ARTICLE ANALYZER] Feedback: {analysis.get('Feedback', '')}")

    # ---------------- ARTICLE RETRY LOOP ----------------
    while not analysis["Approved"]:

        print("\n[WRITER] ❌ Article rejected.")
        print("[WRITER] 🔄 Rewriting article using feedback...")

        article = await writter(analysis["Feedback"])

        print("[WRITER] Improved article created.")

        print("[ARTICLE ANALYZER] Re-analyzing article...")

        article_analysis = await Analyzer(article)
        analysis = json.loads(article_analysis)

        print(f"[ARTICLE ANALYZER] Approved: {analysis['Approved']}")
        print(f"[ARTICLE ANALYZER] Feedback: {analysis.get('Feedback', '')}")

    print("\n[WRITER] ✅ Article approved.")

    # =========================================================
    # EDITING
    # =========================================================
    print("\n[EDITOR] Starting final editing...")

    final = await Editer(article)

    print("[EDITOR] Final version created.")
    print(f"[EDITOR] Type: {type(final)}")
    print(f"[EDITOR] Length: {len(final)}")

    # ---------------- FINAL ANALYSIS ----------------
    print("\n[FINAL ANALYZER] Analyzing edited article...")

    final_analysis = await Analyzer(final)

    print("[FINAL ANALYZER] Raw response:")
    print(final_analysis)

    analysis = json.loads(final_analysis)

    print(f"[FINAL ANALYZER] Approved: {analysis['Approved']}")
    print(f"[FINAL ANALYZER] Feedback: {analysis.get('Feedback', '')}")

    # ---------------- FINAL RETRY LOOP ----------------
    while not analysis["Approved"]:

        print("\n[EDITOR] ❌ Final version rejected.")
        print("[EDITOR] 🔄 Editing again using feedback...")

        final = await Editer(analysis["Feedback"])

        print("[EDITOR] Improved final version created.")

        print("[FINAL ANALYZER] Re-analyzing final version...")

        final_analysis = await Analyzer(final)
        analysis = json.loads(final_analysis)

        print(f"[FINAL ANALYZER] Approved: {analysis['Approved']}")
        print(f"[FINAL ANALYZER] Feedback: {analysis.get('Feedback', '')}")

    print("\n[EDITOR] ✅ Final version approved.")

    # =========================================================
    # FINAL RETURN
    # =========================================================
    print("\n" + "=" * 60)
    print("🎉 PIPELINE COMPLETED SUCCESSFULLY")
    print("=" * 60)

    return final
