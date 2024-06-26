from flask import Blueprint, render_template, request

from models.language_model import LanguageModel
from deep_translator import GoogleTranslator

from models.history_model import HistoryModel

tradutor_controller = Blueprint("tradutor_controller", __name__)


@tradutor_controller.route("/", methods=["GET", "POST"])
def index():
    this_text = request.form.get("text-to-translate")
    acronym_from = request.form.get("translate-from")
    acronym_to = request.form.get("translate-to")
    translated = (
        GoogleTranslator(source=acronym_from, target=acronym_to).translate(
            this_text
        )
        if request.method == "POST"
        else "What do you want to translate?"
    )
    HistoryModel(
        {
            "text_to_translate": this_text,
            "translate_from": acronym_from,
            "translate_to": acronym_to,
            "translated": translated,
        }
    ).save()

    return render_template(
        "index.html",
        languages=LanguageModel.list_dicts(),
        text_to_translate=(this_text if request.method == "POST" else ""),
        translate_from=(acronym_from if request.method == "POST" else "pt"),
        translate_to=(acronym_to if request.method == "POST" else "en"),
        translated=translated,
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
