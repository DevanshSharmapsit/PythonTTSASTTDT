from googletrans import Translator

# Initialize translator
translator = Translator()

print("\n🌐 Welcome to Language Translator 🌐")
print("-----------------------------------")

# Supported language codes
print("Examples of language codes: en (English), hi (Hindi), fr (French), es (Spanish), de (German), ru (Russian), ja (Japanese)")

# Get user input
src_lang = input("\n🔤 Enter source language code: ").strip().lower()
dest_lang = input("🌍 Enter target language code: ").strip().lower()
text = input("📝 Enter the text to translate: ")

try:
    # Translate
    translated = translator.translate(text, src=src_lang, dest=dest_lang)
    print(f"\n✅ Translated Text ({src_lang} → {dest_lang}):\n{translated.text}")
except Exception as e:
    print("❌ Error occurred during translation:", str(e))
