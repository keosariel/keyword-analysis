import json
from keyword_analyzer import ( 
    KeywordAnalyzer, 
    tokenizer, 
    create_model, 
    load_model
)


import os

basedir = os.path.dirname(os.path.abspath(__file__))

def get_data():
    filename = os.path.join(basedir,"data/data1.json")
    
    with open(filename,"r",encoding='utf-8', errors='ignore') as fp:
        data = json.load(fp)
    
    filename = os.path.join(basedir,"data/data2.json")
    with open(filename,"r",encoding='utf-8', errors='ignore') as fp:
        data += json.load(fp)
        
    ret = []
    seen = []
    for d in data:
        d["title"] = d["title"].lower()
        
        t = tokenizer.tokenize(d["title"])
        seen.append(d["title"])
        ret.append(t)
        
    return ret

topics = set([
    "programming",
    "web",
    "software",
    
    # LANGUAGES
    "language", 
    ("language", "languages"),
    "javascript",
    "python",
    "python3",
    ("python","python3"),
    "rust",
    "swift",
    "ruby",
    "html",
    "java",
    "kotlin",
    "css",
    "elixir",
    
    # OPERETING SYSTEMS
    "linux",
    "windows",
    "ios",
    "andriod",
    "os",
    "mobile",
    "desktop",
    
    # FRAMEWORKS
    "framework",
    "react",
    "flutter",
    "nodejs",
    "rails",
    "flask",
    "django",
    "dotnet",
    
    # COMPANIES
    "google",
    "microsoft",
    "apple",
    "github",
    "ibm",
    "amazon",
    "mozilla",
    "twitter",
    "netflix",
    "facebook",
    
    
    # DESIGNS
    "design",
    "frontend",
    ("design","css"),
    "ui",
    
    # DATABASES
    "database",
    ("database","mongodb"),
    ("database","sql"),
    ("database","mysql"),
    ("database","graphql"),
    "sql",
    "mysql",
    "graphql",
    "kubernetes",
    "nosql",
    
    # DATA
    "data",
    ("data","predictions"),
    ("data-science","data","science","&"),
    ("machine-learning","machine","learning","&"),
    ("machine-learning","ml"),
    ("artificial-intelligence","artificial","intelligence","&"),
    ("artificial-intelligence","ai"),
    
    ("open-source","open","source","&"),
    
    # SERVERS
    "server",
    ("server","servers"),
    "aws",
    "heroku",
    "redis",
    "cloud",
    
    # TOOLS
    "tools",
    ("tools","tool"),
    ("vscode","vs"),
    ("vscode","vs","code","&"),
    "chrome",
    "firefox",
    "reviews",
    "browser",
    ("text-editor","editor"),
    "vim",
    "emacs",
    "xcode",
    
    # CAREER
    "job",
    ("job","jobs"),
    "business",
    "startup",
    "productivity",
    
    # LEARN
    "algorithm",
    ("algorithm", "algorithms"),
    "performance",
    "beginners",
    
    # SECURITY
    "security",
    ("security","cryptography"),
    ("security","cybersecurity"),
    ("security","encryption"),
    
    # OTHER
    "api",
    "application",
    "ask",
    "crypto",
    "community",
    "library",
    "platforms",
    "practices",
    "security",
    "news",
    "how-to",
    "game",
    ("game","gaming"),
    "youtube",
    "socket",
    "science",
    "apps",
    "alternative",
    ("alternative","alternatives"),
    
    "covid",  
])

KEYWORD_MODEL_FILE = os.path.join(basedir,"tagger.pkl") 


# Instantiating Keyword Analysis class and saving it
docs = get_data()
KEYWORD_MODEL = create_model(KEYWORD_MODEL_FILE,docs,topics)

# Load if you have saved it
# KEYWORD_MODEL = load_model(KEYWORD_MODEL_FILE)
