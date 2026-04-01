# -*- coding: utf-8 -*-
"""
Aplica copy de Recetas Hígado Graso ao elementor-149-2026-03-23-updated.json
sem recriar a estrutura — só edita settings dos widgets existentes.
"""
import copy
import json
import pathlib

SRC = pathlib.Path(__file__).parent / "elementor-149-2026-03-23-updated.json"
CHECKOUT = "https://SEU-LINK-HOTMART.com"

# Faixa animada (widget html 3b5abac4) — mesma estrutura CSS do modelo, copy nova
MARQUEE_HTML = """<style>
.marquee {
  overflow: hidden;
  width: 100%;
  padding: 24px 0;
}
.marquee__inner {
  display: flex;
  gap: 64px;
  width: max-content;
  animation: marquee 50s linear infinite;
}
.marquee-item {
  min-width: 520px;
  font-size: 18px;
  line-height: 1.6;
  font-weight: 500;
  color: #ffffff;
  white-space: normal;
}
.marquee-item strong {
  font-weight: 700;
  color: #ffffff;
}
.marquee-item span {
  font-weight: 700;
  background: linear-gradient(90deg, #f97316, #ec4899);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  color: transparent;
}
@keyframes marquee {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}
@media (max-width: 768px) {
  .marquee-item {
    min-width: 300px;
    font-size: 16px;
  }
}
</style>
<div class="marquee">
  <div class="marquee__inner">
    <div class="marquee-item">
      <span>Recetas para hígado graso</span> — acceso digital inmediato tras la compra.
    </div>
    <div class="marquee-item">
      Platos en <strong>menos de 30 minutos</strong>, ingredientes de mercado y opciones para toda la familia.
    </div>
    <div class="marquee-item">
      <span>Guía práctica en español</span> — claridad en el plato, sin dietas imposibles.
    </div>
    <div class="marquee-item">
      <span>Recetas para hígado graso</span> — acceso digital inmediato tras la compra.
    </div>
    <div class="marquee-item">
      Platos en <strong>menos de 30 minutos</strong>, ingredientes de mercado y opciones para toda la familia.
    </div>
    <div class="marquee-item">
      <span>Guía práctica en español</span> — claridad en el plato, sin dietas imposibles.
    </div>
  </div>
</div>"""

# Patches: widget_id -> chaves dentro de settings (merge)
# Nota: não incluir 750cf1ab — preserva o script de tracking que já está no JSON.
PATCHES = {
    "3b5abac4": {"html": MARQUEE_HTML},
    "77867c2d": {
        "title": "🌿 COCINA ACTIVA — Guía de recetas",
    },
    "7d82fd4f": {
        "title": "Para quienes quieren comer rico y cuidar su hígado sin dietas imposibles:",
    },
    "16326d2e": {
        "title": "Recetas Deliciosas para Curar el Hígado Graso",
    },
    "21d6dda6": {
        "editor": "<p>Come delicioso, reduce la carga sobre tu hígado y recupera energía — <strong>sin aburrirte en la cocina</strong> ni depender de listas confusas de internet.</p>",
    },
    "e021337": {
        "html": '<div style="text-align:center;max-width:560px;margin:0 auto;">'
        '<img src="img/recetas.webp" alt="Recetas saludables para hígado graso" style="width:100%;max-width:520px;border-radius:16px;box-shadow:0 12px 40px rgba(0,0,0,0.15);" loading="lazy" />'
        "</div>"
    },
    "20f47c6f": {
        "text": "🌿 QUIERO MIS RECETAS AHORA",
        "link": {
            "url": CHECKOUT,
            "is_external": "on",
            "nofollow": "",
            "custom_attributes": "",
        },
    },
    "73228ced": {
        "editor": "<p>Acceso digital inmediato • Recetas en menos de 30 min • Ingredientes de mercado</p>",
    },
    "6a3b84a8": {
        "title": "¿Tu médico dijo “dieta” pero no te explicó qué comer?",
    },
    "4c19a5c0": {
        "editor": "<p>Si tienes hígado graso, seguramente te suena: información contradictoria en Google, miedo a que empeore, cansancio e hinchazón… y ganas de hacerlo bien, sin adivinar.</p>"
        "<p>Lo que falta no es “más fuerza de voluntad”: es un <strong>plan claro de platos</strong> que puedas sostener.</p>",
    },
    "57954f3d": {
        "editor": '<blockquote><p>“Probé dietas insípidas y las dejé. Necesitaba algo que supiera a comida de verdad, no a hospital.”</p></blockquote>',
    },
    "5dcded66": {
        "editor": "<p>Por eso reunimos recetas pensadas para el hígado graso: sabrosas, prácticas y organizadas por momentos del día — para que sepas <strong>qué cocinar mañana</strong>, no solo qué evitar.</p>",
    },
    "44d855f5": {
        "title": "¿Por qué tantas personas se frustran… y esta guía sí funciona en el día a día?",
    },
    "6ef4dbe1": {
        "title": "❌ Sin un plan claro<br>(improvisar o buscar en Google)",
    },
    "27d1694f": {
        "editor": '<div class="audience-card"><p>❌ Listas contradictorias y estrés en la cocina.</p>'
        '<p>❌ Recetas genéricas que no están pensadas para el hígado.</p>'
        '<p>❌ Mucho tiempo buscando… y poco cocinando.</p>'
        '<p>❌ Sensación de culpa cada vez que comes.</p>'
        '<p>❌ Cansancio que no mejora porque el plato no acompaña.</p></div>',
    },
    "5ddbaf66": {
        "title": "✅ Con la guía de recetas<br>(paso a paso)",
    },
    "626b0c24": {
        "editor": '<div class="audience-card"><p>✅ Desayuno, almuerzo, merienda y cena <strong>alineados</strong> a tu objetivo.</p>'
        '<p>✅ Qué priorizar y qué reducir, explicado sin vueltas.</p>'
        '<p>✅ Platos rápidos (menos de 30 minutos).</p>'
        '<p>✅ Ingredientes accesibles en cualquier mercado.</p>'
        '<p>✅ Tu familia puede comer lo mismo: no cocinas dos veces.</p></div>',
    },
    "3de0bbe": {
        "title": "🎯 ¿Para quién es esta guía?",
    },
    "000c1dd": {
        "editor": '<p style="font-size:18px;">👉 <strong>Personas con hígado graso (NAFLD)</strong> que quieren ordenar su plato sin sentirse perdidas.</p><br>'
        '<p style="font-size:18px;">👉 <strong>Quienes tienen triglicéridos o colesterol alto</strong> y buscan recetas coherentes con su metabolismo.</p><br>'
        '<p style="font-size:18px;">👉 <strong>Familias ocupadas</strong> que necesitan recetas rápidas y sabrosas, no “comida de régimen”.</p>',
    },
    "7b7c760a": {
        "title": "👇 Qué incluye tu acceso hoy",
    },
    "45065503": {
        "editor": "<p>Al adquirir <strong>Recetas Deliciosas para Curar el Hígado Graso</strong> recibes:</p>",
    },
    "255f7f62": {
        "editor": "<h4><strong>✔️ Guía completa de recetas</strong></h4>"
        "<p>Desayunos, almuerzos, snacks y cenas diseñados para nutrir y apoyar tu hígado, con variedad real.</p><br>"
        '<h4><strong>✔️ Lista clara de alimentos</strong></h4>'
        "<p>Qué conviene priorizar y qué conviene reducir, con explicación directa.</p>",
    },
    "58e8dad5": {
        "editor": "<h4><strong>✔️ Información práctica</strong></h4>"
        "<p>Preparaciones en menos de 30 minutos para quien tiene poco tiempo.</p>",
    },
    "55f8d9d3": {
        "editor": "<h4><strong>✔️ Enfoque familiar</strong></h4>"
        "<p>Recetas que todos pueden disfrutar — sin cocinar dos menús distintos.</p>",
    },
    "6b8f41cc": {
        "editor": "<h4><strong>✔️ Base nutricional</strong></h4>"
        "<p>Para entender por qué cada receta te ayuda en tu objetivo de bienestar hepático.</p>"
        "<br><h4><strong>✔️ Acceso digital</strong></h4>"
        "<p>Lee desde el móvil o la computadora cuando quieras.</p>",
    },
    "2e335ea": {
        "title": "Lo que dicen quienes ya aplicaron las recetas",
    },
    "0cee529": {
        "image": {
            "url": "img/testimonio-1.webp",
            "id": "",
        }
    },
    "977685a": {
        "image": {
            "url": "img/testimonio-2.webp",
            "id": "",
        }
    },
    "cdc1f80": {
        "image": {
            "url": "img/testimonio-3.webp",
            "id": "",
        }
    },
    "b9d6b83": {
        "title": "🎁 BONUS: estructura semanal para no improvisar",
    },
    "05ea65e": {
        "editor": '<p style="text-align:center;font-size:20px;color:#D97706;"><em>(Organiza tu semana sin pensar “¿y ahora qué como?”)</em></p><br>'
        '<p style="text-align:center;font-size:18px;">Incluye enfoque práctico para armar tu rutina de comidas y reducir la ansiedad por la comida.</p>',
    },
    "761aa134": {"title": "Cómo empezar (simple)"},
    "17f2036d": {
        "image": {
            "url": "img/mockup.webp",
            "id": "",
        }
    },
    "5aaf031a": {"title": "1. Accede al material"},
    "53f5c91e": {
        "editor": "<p>Recibes el acceso por email. Abres la guía en tu celular o computadora — sin complicaciones.</p>",
    },
    "62a0a98": {
        "image": {
            "url": "img/mockup.webp",
            "id": "",
        }
    },
    "5d21cf6c": {"title": "2. Elige recetas por momento del día"},
    "5a5cd511": {
        "editor": "<p>Desayuno, almuerzo, merienda o cena: sigue el plan que encaja con tu rutina.</p>",
    },
    "233fe587": {
        "image": {
            "url": "img/recetas.webp",
            "id": "",
        }
    },
    "5c18d7e": {"title": "3. Cocina y mantén el hábito"},
    "7aadbed4": {
        "editor": "<p>Platos sabrosos que te ayudan a sostener el cambio — la clave es constancia, no perfección.</p>",
    },
    "1a862c63": {"title": "Tu salud hepática vale la inversión"},
    "5694b646": {
        "editor": "<blockquote><p>Cada semana sin un plan claro es una semana improvisando — y el estrés también cuenta.</p>"
        "<p>Esta guía te devuelve <strong>claridad</strong>: qué comprar y qué cocinar.</p></blockquote>",
    },
    "230d3fd4": {
        "editor": '<p style="text-align:center;"><strong>Una inversión pequeña comparada con meses de ensayo y error.</strong></p>',
    },
    "241ac949": {"title": "Elige tu acceso"},
    "4c44f7d2": {"title": "Oferta digital"},
    "2186bd1d": {
        "title": '<span style="font-size:42px;font-weight:800;color:#2563eb;">16 US$</span> '
        '<span style="font-size:18px;color:#6b7280;"> / acceso</span>',
    },
    "6eb54d10": {
        "editor": "<p>Guía en PDF/formato digital con recetas para el hígado graso.</p>",
    },
    "7005a09": {
        "editor": "<p>✅ Recetas por momentos del día<br>✅ Lista práctica de alimentos<br>✅ Platos rápidos<br>✅ Enfoque familiar<br>✅ Acceso online<br>✅ Actualizaciones incluidas</p>",
    },
    "7fc3456c": {
        "text": "Quiero acceder ahora",
        "link": {
            "url": CHECKOUT,
            "is_external": "on",
            "nofollow": "",
            "custom_attributes": "",
        },
    },
    "7facd82f": {"title": "🔥 OFERTA ESPECIAL"},
    "9183e84": {"title": "PACK COMPLETO"},
    "505141d9": {
        "title": '<span style="font-size:42px;font-weight:800;color:#000;">64 US$</span> '
        '<span style="font-size:16px;color:#6b7280;">precio referencia</span> '
        '<br><span style="font-size:36px;font-weight:800;color:#f59e0b;">16 US$</span> '
        '<span style="font-size:16px;">hoy</span>',
    },
    "62cda1c7": {"editor": "<p>Pago único — acceso al material digital.</p>"},
    "2dd2abca": {
        "editor": "<p>✅ Todo el contenido de la guía<br>✅ Bonus de organización<br>✅ Soporte por email<br>✅ Garantía de satisfacción</p>",
    },
    "7eb7d47c": {
        "text": "Comprar ahora",
        "link": {
            "url": CHECKOUT,
            "is_external": "on",
            "nofollow": "",
            "custom_attributes": "",
        },
    },
    "28c2eb5f": {"title": "Solo guía (básico)"},
    "53cc37c5": {
        "title": '<span style="font-size:38px;font-weight:800;color:#2563eb;">9 US$</span> '
        '<span style="font-size:15px;color:#6b7280;">/módulo intro</span>',
    },
    "760c1c93": {"editor": "<p>Si quieres empezar con un módulo reducido (cuando aplique en tu funnel).</p>"},
    "38f1c284": {"editor": "<p>✅ Contenido parcial según oferta<br>✅ Acceso digital</p>"},
    "6396f38": {
        "text": "Ver opción",
        "link": {
            "url": CHECKOUT,
            "is_external": "on",
            "nofollow": "",
            "custom_attributes": "",
        },
    },
    "6436bd2a": {
        "editor": "<blockquote><h3 style=\"text-align:center;\">⏳ Cada día sin plan es un día improvisando.</h3>"
        "<p style=\"text-align:center;\">Si estás leyendo esto, ya sabes que tu hígado necesita un cambio real — no otro “lunes empiezo”.</p></blockquote>",
    },
    "c2ce6c7": {"title": "🛡️ Garantía 60 días"},
    "217c18c": {
        "editor": "<p style=\"text-align:center;font-size:18px;\">Tienes 60 días para revisar el material. Si no es lo que esperabas, solicitas reembolso según las reglas de la plataforma.</p>",
    },
    "4c97f97a": {"title": "Preguntas frecuentes"},
    "5d57e44a": {"title": "Recetas Deliciosas — Hígado Graso"},
    "58999912": {
        "editor": "<p>Guía práctica en español para organizar tu alimentación con foco hepático.</p>",
    },
    "14f8a99a": {
        "text": "Quiero las recetas ahora",
        "link": {
            "url": CHECKOUT,
            "is_external": "",
            "nofollow": "",
            "custom_attributes": "",
        },
    },
    "7abb2ae4": {
        "editor": "<p>Acceso digital • Material descargable/consulta online • Garantía según plataforma</p>",
    },
    "44898960": {
        "editor": "<p>© 2026 Recetas Deliciosas para Curar el Hígado Graso. Contenido educativo; no sustituye consejo médico.</p>",
    },
}

# FAQ nested-accordion: títulos en orden
FAQ_TITLES = [
    "¿Por cuánto tiempo tengo acceso al contenido?",
    "¿Cómo accedo al material?",
    "¿Qué pasa si necesito ayuda?",
    "¿Cuánto tardan en enviarme el material?",
    "¿Necesito ser experto en cocina?",
    "¿Sirve si tengo diabetes o colesterol alto?",
]

FAQ_ANSWERS = [
    "<p>Acceso de por vida al material y actualizaciones futuras según se indique en la compra.</p>",
    "<p>Recibirás el enlace por email para acceder desde celular o computadora.</p>",
    "<p>Podrás contactar soporte según las vías indicadas en tu correo de compra.</p>",
    "<p>El acceso es inmediato tras confirmar el pago.</p>",
    "<p>No. Las recetas están explicadas paso a paso.</p>",
    "<p>Sí: muchas personas con hígado graso también tienen perfil metabólico asociado; las recetas están pensadas con ese contexto. Consulta a tu médico para tu caso.</p>",
]


def deep_merge_settings(base, patch):
    """Merge recursivo sólo um nível em dicts aninhados comuns."""
    for k, v in patch.items():
        if k in base and isinstance(base[k], dict) and isinstance(v, dict):
            deep_merge_settings(base[k], v)
        else:
            base[k] = v


def walk_patch(obj):
    if isinstance(obj, dict):
        eid = obj.get("id")
        if obj.get("elType") == "widget" and eid in PATCHES:
            if "settings" not in obj:
                obj["settings"] = {}
            deep_merge_settings(obj["settings"], PATCHES[eid])

        # nested-accordion FAQ
        if (
            obj.get("elType") == "widget"
            and obj.get("widgetType") == "nested-accordion"
            and eid == "4260ba37"
        ):
            st = obj.setdefault("settings", {})
            items = st.get("items") or []
            for i, it in enumerate(items):
                if i < len(FAQ_TITLES):
                    it["item_title"] = FAQ_TITLES[i]
            # elementos filhos: editores em ordem DFS dos containers locked
            eds = []

            def collect_editors(o):
                if isinstance(o, dict):
                    if o.get("elType") == "widget" and o.get("widgetType") == "text-editor":
                        eds.append(o)
                    for v in o.values():
                        collect_editors(v)
                elif isinstance(o, list):
                    for x in o:
                        collect_editors(x)

            collect_editors(obj.get("elements", []))
            for i, w in enumerate(eds):
                if i < len(FAQ_ANSWERS):
                    w.setdefault("settings", {})["editor"] = FAQ_ANSWERS[i]

        for v in obj.values():
            walk_patch(v)
    elif isinstance(obj, list):
        for item in obj:
            walk_patch(item)


def main():
    data = json.loads(SRC.read_text(encoding="utf-8"))
    data = copy.deepcopy(data)
    walk_patch(data["content"])
    data["title"] = "LP Recetas Hígado Graso — ES (modelo 149)"
    out_path = SRC.parent / "elementor-149-2026-03-23-updated.json"
    out_path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    print("OK:", out_path)


if __name__ == "__main__":
    main()
