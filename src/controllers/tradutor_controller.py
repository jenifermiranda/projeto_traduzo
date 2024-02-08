from flask import Blueprint, render_template, request

from models.language_model import LanguageModel
from deep_translator import GoogleTranslator

tradutor_controller = Blueprint("tradutor_controller", __name__)


@tradutor_controller.route("/", methods=["GET", "POST"])
def index():
    this_text = request.form.get("text-to-translate")
    acronym_from = request.form.get("translate-from")
    acronym_to = request.form.get("translate-to")

    return render_template(
        "index.html",
        languages=LanguageModel.list_dicts(),
        text_to_translate=(
            request.form.get("text-to-translate")
            if request.method == "POST"
            else "O que deseja traduzir?"
        ),
        translate_from=(
            request.form.get("translate-from")
            if request.method == "POST"
            else "pt"
        ),
        translate_to=(
            request.form.get("translate-to")
            if request.method == "POST"
            else "en"
        ),
        translated=(
            GoogleTranslator(source=acronym_from, target=acronym_to).translate(
                this_text
            )
            if request.method == "POST" and this_text is not None
            else "What do you want to translate?"
        ),
    )


@tradutor_controller.route("/reverse", methods=["POST"])
def index_reverse():
    this_text = request.form.get("text-to-translate")
    acronym_from = request.form.get("translate-from")
    acronym_to = request.form.get("translate-to")

    return render_template(
        "index.html",
        languages=LanguageModel.list_dicts(),
        text_to_translate=GoogleTranslator(
            source=acronym_from, target=acronym_to
        ).translate(this_text),
        translate_from=request.form.get("translate-to"),
        translate_to=request.form.get("translate-from"),
        translated=request.form.get("text-to-translate"),
    )
