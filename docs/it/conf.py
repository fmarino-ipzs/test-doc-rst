#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# -- Variabili di PROGETTO ----------------------------------------------------
settings_project_name = "Documentazione Tecnica"
settings_editor_name = 'FAM'
settings_doc_version = '1.0.0'
settings_doc_release = "versione-corrente"
settings_basename = 'technical-docs'
settings_file_name = 'technical-docs'

version = settings_doc_version


import sys, os
from pathlib import Path
confdir = Path(__file__).resolve().parent
# -- Configurazione RTD -------------------------------------------------

# on_rtd indica se siamo su readthedocs.org, questa linea di codice è presa da docs.readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

# Questo è usato per i collegamenti e simili in modo da collegare alla cosa che stiamo costruendo
rtd_version = os.environ.get('READTHEDOCS_VERSION', 'latest')
if rtd_version not in ['stable', 'latest']:
    rtd_version = 'latest'

rtd_project = os.environ.get('READTHEDOCS_PROJECT', '')

# Se le estensioni (o moduli da documentare con autodoc) sono in un'altra directory,
# aggiungi queste directory a sys.path qui. Se la directory è relativa alla
# radice della documentazione, usa os.path.abspath per renderla assoluta, come mostrato qui.
#sys.path.insert(0, os.path.abspath('.'))

# -- Configurazione generale -----------------------------------------------------

# Se la tua documentazione necessita di una versione minima di Sphinx, indicala qui.
needs_sphinx = '7.0'

# Aggiungi qui qualsiasi nome del modulo di estensione Sphinx, come stringhe. Possono essere
# estensioni che vengono con Sphinx (denominate 'sphinx.ext.*') o tue personalizzate.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.ifconfig',
    'sphinx.ext.autosectionlabel',
    'sphinxcontrib.redoc',
    'myst_parser',
    'sphinxcontrib.plantuml',  
]

plantuml_jar = confdir.parent.parent / "utils/plantuml/plantuml-1.2025.2.jar"
plantuml = f'java -jar {str(plantuml_jar)}'
plantuml_output_format = 'svg'
plantuml_latex_output_format = 'pdf'

images_config = {
    "default_image_width": "99%",
    "align": "center"
}

# Aggiungi qui qualsiasi percorso che contiene modelli, relativi a questa directory.
templates_path = ['_templates']

# Il suffisso dei nomi dei file sorgente.
source_suffix = ['.rst', '.md']

# La codifica dei file sorgente.
#source_encoding = 'utf-8-sig'
source_encoding = 'utf-8'

# Il documento principale toctree.
master_doc = 'index'

# Informazioni generali sul progetto.
project = settings_project_name
# copyright = settings_copyright_copyleft

# URL dell'istanza Discourse utilizzata dall'estensione sphinxcontrib.discourse
# discourse_url = settings_discourse_url

# Le informazioni sulla versione per il progetto che stai documentando, fungono da sostituzione per
# |version| e |release|, usate anche in vari altri posti nei
# documenti costruiti.
#
# La versione breve X.Y.
# version = settings_doc_version
# La versione completa, inclusi tag alpha/beta/rc.
# release = settings_doc_release

# La lingua per i contenuti autogenerati da Sphinx. Fare riferimento alla documentazione
# per un elenco di lingue supportate.
language = 'it'

# Ci sono due opzioni per sostituire |today|: o imposti today su qualche
# valore non falso, quindi viene utilizzato:
#today = ''
# Altrimenti, today_fmt viene utilizzato come formato per una chiamata strftime.
#today_fmt = '%B %d, %Y'

# Elenco di modelli, relativi alla directory sorgente, che corrispondono a file e
# directory da ignorare quando si cercano file sorgente.
exclude_patterns = ['.DS_Store', 'README', 'README.md', '.venv*', '.env*']

# Il nome dello stile Pygments (evidenziazione della sintassi) da utilizzare.
pygments_style = 'sphinx'

# -- Configurazione myst-parser --------------------------------------------------------
# Configurazione per myst_parser che sostituisce recommonmark
myst_enable_extensions = [
    "colon_fence",
    "smartquotes",
    "replacements",
    "deflist",
]

# Configurazione simile ad AutoStructify di recommonmark
myst_heading_anchors = 3
myst_enable_auto_toc_tree = True
myst_update_mathjax = False

# -- Opzioni per l'output HTML ----------------------------------------------
html_theme = 'piccolo_theme'

# html_theme_path = [docs_italia_theme.get_html_theme_path()]

# Le opzioni del tema sono specifiche del tema e personalizzano l'aspetto di un tema
# ulteriormente. Per un elenco di opzioni disponibili per ciascun tema, consulta la
# documentazione.
html_theme_options = {
    # Questa opzione può essere utilizzata con docs-italia-theme per personalizzare come viene mostrato il badge delle versioni:
    # 'False': badge predefinito (alabaster) | 'True': badge personalizzato (italia)
    # 'custom_versions_badge': True,
    #'collapse_navigation': True,
    "show_theme_credit": False,
    "source_url": 'https://github.com/fmarino-ipzs/test-doc-rst/',
    "source_icon": "github",
    # "banner_text": 'Abbiamo appena lanciato una newsletter, <a href="https://mynewsletter.com/">iscriviti</a>!'
}



# Il nome per questo insieme di documenti Sphinx. Se None, diventa predefinito a
# "<project> v<release> documentation".
html_title = f"{settings_project_name} - {version}"

# Un titolo più breve per la barra di navigazione. Il predefinito è lo stesso di html_title.
# html_short_title = "IT-Wallet"

# Il nome di un file di immagine (relativo a questa directory) da posizionare nella parte superiore
# della barra laterale.
# html_logo = "https://avatars.githubusercontent.com/u/15377824?s=48&v=4"

# Il nome di un file di immagine (all'interno del percorso statico) da utilizzare come favicon dei
# documenti. Questo file dovrebbe essere un file di icona Windows (.ico) di 16x16 o 32x32
# pixel.
#html_favicon = ""

# Aggiungi qui qualsiasi percorso che contenga file statici personalizzati (come fogli di stile), qui,
# relativi a questa directory. Vengono copiati dopo i file statici incorporati,
# quindi un file denominato "default.css" sovrascriverà il "default.css" incorporato.
#html_static_path = ['../../static']

# Aggiungi qui qualsiasi percorso extra che contenga file personalizzati (come robots.txt o
# .htaccess), qui, relativi a questa directory. Questi file vengono copiati
# direttamente nella radice della documentazione.
# html_extra_path = ["../common"]

# Se non è '', un timestamp 'Ultimo aggiornamento il:' viene inserito in fondo a ogni pagina,
# utilizzando il formato strftime specificato.
html_last_updated_fmt = '%d/%m/%Y'

# Se true, SmartyPants verrà utilizzato per convertire virgolette e trattini in
# entità tipograficamente corrette.
#html_use_smartypants = True

# Modelli di barra laterale personalizzati, mappa i nomi dei documenti ai nomi dei modelli.
#html_sidebars = {}

# Modelli aggiuntivi che dovrebbero essere renderizzati nelle pagine, mappa i nomi delle pagine ai
# nomi dei modelli.
#html_additional_pages = {}

# Se false, non viene generato alcun indice del modulo.
#html_domain_indices = True

# Se false, non viene generato alcun indice.
#html_use_index = True

# Se true, l'indice è diviso in pagine individuali per ogni lettera.
#html_split_index = False

# Se true, i collegamenti alle fonti reST vengono aggiunti alle pagine.
#html_show_sourcelink = True

# Se true, "Creato usando Sphinx" viene mostrato nel piè di pagina HTML. Il valore predefinito è True.
#html_show_sphinx = True

# Se true, "(C) Copyright ..." viene mostrato nel piè di pagina HTML. Il valore predefinito è True.
html_show_copyright = False

# Se true, verrà generato un file di descrizione OpenSearch e tutte le pagine conterranno
# un tag <link> che vi fa riferimento. Il valore di questa opzione deve essere l'
# URL base da cui viene servito l'HTML finito.
#html_use_opensearch = ''

# Questo è il suffisso del nome del file per i file HTML (ad es. ".xhtml").
#html_file_suffix = None

# Nome del file di base di output per il costruttore di aiuto HTML.
htmlhelp_basename = settings_basename + 'doc'


# -- Opzioni per l'output LaTeX ---------------------------------------------

latex_elements = {
# La dimensione della carta ('letterpaper' o 'a4paper').
'papersize': 'a4paper',

# La dimensione del carattere ('10pt', '11pt' o '12pt').
'pointsize': '10pt',

'sphinxsetup': 'verbatimforcewraps=true',

# Roba aggiuntiva per il preambolo LaTeX.
#'preamble': '',
}

# Raggruppamento dell'albero del documento in file LaTeX. Elenco di tuple
# (file di inizio sorgente, nome di destinazione, titolo,
# autore, classe di documento [howto, manual, o classe personalizzata]).
latex_documents = [
  ('index', settings_file_name + '.tex', settings_project_name, settings_editor_name, 'manual'),
]

# Il nome di un file di immagine (relativo a questa directory) da posizionare nella parte superiore di
# la pagina del titolo.
#latex_logo = "https://avatars.githubusercontent.com/u/15377824?s=48&v=4"

# Per i documenti "manual", se questo è true, allora le intestazioni di primo livello sono parti,
# non capitoli.
latex_use_parts = True

# Se true, mostra i riferimenti di pagina dopo i collegamenti interni.
latex_show_pagerefs = True

# Se true, mostra gli indirizzi URL dopo i collegamenti esterni.
latex_show_urls = "inline"

# Documenti da aggiungere come appendice a tutti i manuali.
#latex_appendices = []

# Se false, non viene generato alcun indice del modulo.
#latex_domain_indices = True

# -- Opzioni per l'output della pagina del manuale ---------------------------------------

# Una voce per pagina del manuale. Elenco di tuple
# (file di inizio sorgente, nome, descrizione, autori, sezione del manuale).
man_pages = [
    ('index', settings_file_name, settings_project_name,
     [settings_editor_name], 1)
]

# Se true, mostra gli indirizzi URL dopo i collegamenti esterni.
#man_show_urls = False


# -- Opzioni per l'output Texinfo -------------------------------------------

# Raggruppamento dell'albero del documento in file Texinfo. Elenco di tuple
# (file di inizio sorgente, nome di destinazione, titolo, autore,
# voce di menu dir, descrizione, categoria)
texinfo_documents = [
  (
    'index',
    settings_file_name,
    settings_project_name,
    settings_project_name,
    settings_project_name,
    'Varie'
  )
]

numfig = True

# per disattivare smartquotes e poterli utilizzare
smartquotes = False

autosectionlabel_prefix_document= True


# # Funzione per convertire SVG in PDF
# def convert_svg_to_pdf(srcdir):
#     """Converte tutti i file SVG nella directory di origine in PDF usando Python"""
#     # Rileva la directory dei sorgenti

#     print(f"Cercando SVG in {srcdir}")
    
#     # Trova tutti i file SVG
#     svg_files = []
#     for root, dirs, files in os.walk(srcdir):
#         for file in files:
#             if file.endswith('.svg'):
#                 svg_files.append(os.path.join(root, file))
    
#     print(f"Trovati {len(svg_files)} file SVG")
    
#     # Usa svglib per convertire
#     svglib_available = False
#     try:
#         from svglib.svglib import svg2rlg
#         from reportlab.graphics import renderPDF
#         svglib_available = True
#         print("Utilizzo svglib per la conversione SVG→PDF")
#     except ImportError:
#         print("svglib non disponibile")
    
#     # Converti ogni SVG in PDF
#     for svg_file in svg_files:
#         pdf_file = svg_file.replace('.svg', '.pdf')
#         converted = False
        
#         # Prova prima con svglib se disponibile
#         if svglib_available:
#             try:
#                 print(f"Conversione con svglib: {svg_file} → {pdf_file}")
#                 drawing = svg2rlg(svg_file)
#                 renderPDF.drawToFile(drawing, pdf_file)
#                 print(f"✓ Convertito con successo usando svglib")
#                 converted = True
#             except Exception as e:
#                 print(f"✗ Errore nella conversione con svglib: {e}")
#         if not converted:
#             print(f"! Impossibile convertire {svg_file} in PDF con gli strumenti disponibili")

# # Collegamento evento solo se siamo in modalità LaTeX
# def setup(app):
#     app.connect('builder-inited', on_builder_init)
#     confdir = app.confdir  # Directory di configurazione
#     return {
#         'version': '0.1',
#         'parallel_read_safe': True,
#         'parallel_write_safe': True,
#     }

# def on_builder_init(app):
#     if app.builder.name == 'latex':
#         imgdir = os.path.join(app.confdir,'../../images')   # Directory sorgente
#         srcdir = app.srcdir  # Directory sorgente
#         confdir = app.confdir  # Directory di configurazione
#         outdir = app.outdir  # Directory di output
#         print(f"Directory di configurazione: {confdir}")
#         print(f"Directory sorgente: {srcdir}")
#         print(f"Directory output: {outdir}")
#         print(f"Directory sorgente: {imgdir}")
#         try:
#             convert_svg_to_pdf(imgdir)
#         except Exception as e:
#             print(f"Errore durante la conversione SVG→PDF: {e}")
#             print("Il processo di build continuerà, ma le immagini SVG potrebbero non apparire nel PDF.")