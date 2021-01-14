import json
from keyword_analyzer import ( 
    KeywordAnalyzer, 
    tokenizer, 
    create_model, 
    load_model
)


import os

basedir = ""

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
        #if d["title"] not in seen:
        t = tokenizer.tokenize(d["title"])
        seen.append(d["title"])
        ret.append(t)
        
    return ret
'''
lib
language
'''

TOPIC_MAP = {
    "machinelearning" : "machine-learning",
    "tutorial" : "tutorial",
    "node"     : ["nodejs","javascript","webdev"],
    "nodejs"     : ["nodejs","javascript","webdev"],
    "react"    : ["react","javascript","webdev"],
    "opensource" : "open-source",
    "cpp"        : "cpp",
    "programming" : "programming",
    "tailwindcss" : ["tailwindcss","css","frontend","design","webdev"],
    "seo"         : "seo",
    "career"      : "career",
    "careers"     : "career",
    "developer"   : "developer",
    "developers"  : "developer",
    "cryptocurrency": "cryptocurrency",
    "bitcoin"       : ["cryptocurrency", "bitcoin"],
    "btc"       : ["cryptocurrency", "bitcoin"],
    "ethereum"   : ["cryptocurrency", "ethereum"],
    "entrepreneurship": "entrepreneurship",
    "technology"      : "technology",
    "vr"               : ["technology","vr"],
    "ar"               : ["technology","ar"],
    "cybersecurity"    : ["security","cybersecurity"],
    "startups"         : "startups",
    "web development"  : "webdev",
    "html5"            : "html",
    "blogging"         : "blogging",
    "blog"          : "blogging",
    "algorithms"    : "algorithms",
    "node.js"       : "nodejs",
    "cli": "cli",
    "laravel":"laravel",
    "software development":"software",
    "linux":["linux","os"],
    "aws":["aws","server"],
    "redis":["redis","server"],
    "bootstrap":["bootstrap","css","frontend","design","webdev"],
    "codenewbie":["codenewbie","learn"],
    "unix"      : ["unix","os"],
    "npm":"npm",
    "productivity":"productivity",
    "iot":["iot","technology"],
    "web-scraping":"programming",
    "coding":"programming",
    "how-to":["how-to","learn","tutorial"],
    "ux":["ux","design"],
    "ui":["ui","design"],
    "big-data":["big-data","data"],
    "encryption":["security"],
    "bug-bounty":["bug-bounty","hacking"],
    "visualization":["data-visualization","data-science"],
    "data-visualization":["data-visualization","data-science"],
    "review":"review",
    "vim":["vim","terminal","text-editor","tools"],
    "emacs":["emacs","terminal","text-editor","tools"],
    "vscode":["vscode","tools"],
    "tool":["tools"],
    "tools":["tools"],
    "programing":"programming",
    "graphql":["graphql","database"],
    "postgresql":["postgresql","database"],
    "mongodb":["mongodb","database"],
    "sql":["sql","database"],
    "nosql":["nosql","database"],
    "learn-to-code":["learn","codenewbie"],
    "learning":["learn"],
    "metro":["metro","javascript"],
    "flask":["flask","python","webdev"],
    "django":["django","python","webdev"],
    "interview":"interview",
    "interviews":"interview",
    "statistics":["statistics","data-science"],
    "probability":["probability","statistics","data-science"],
    "tech":["technology"],
    "business":"business",
    "math":["mathematics"],
    "function":"function",
    "freelancer":"freelancing",
    "freelancers":"freelancing",
    "freelancing":"freelancing",
    "pandas":["pandas","data-science","python"],
    "serverless":["serverless","webdev"],
    "privacy":"privacy",
    "bugs":["debugging"],
    "debugs":["debugging"],
    "debug":["debugging"],
    "markdown":"markdown",
    "engineering":"engineering",
    "ml-engineering":"engineering",
    "health":"health",
    "healthcare":"health",
    "malware":["malware","security"],
    "samsung":"samsung",
    "news":"news",
    "web-development":"webdev",
    "webdev":"webdev",
    "design":"design",
    "artificial-intelligence":["artificial-intelligence"],
    "machine-learning":["machine-learning"],
    "artificial intelligence":["artificial-intelligence"],
    "machine learning":["machine-learning"],
    "ai":["artificial-intelligence"],
    "ml":["machine-learning"],
    "nlp":["nlp","machine-learning"],
    "detection":["detection","artificial-intelligence"],
    "data structures":["data-structures","algorithms"],
    "data-structures":["data-structures","algorithms"],
    "deep-learning":["deep-learning","machine-learning"],
    "facedetection":["facedetection","deep-learning","machine-learning"],
    "github":"github",
    "vue":["vue","javascript"],
    "gatsby":["gatsby","javascript"],
    "ubuntu":["ubuntu","linux"],
    "beginners":["beginners","learn"],
    "beginner":["beginners","learn"],
    "gaming":"gaming",
    "xbox"  :["xbox","gaming"],
    "blockchain":"blockchain",
    "data-mining":["data-mining","data"],
    "datamining":["data-mining","data"],
    "web-monetization":"web-monetization",
    "firebase" : "firebase",
    "full stack":["full-stack"],
    "full-stack":["full-stack"],
    "fullstack":["full-stack"],
    "opencv":"opencv",
    "finance":"finance",
    "performance":"performance",
    "netlify":"netlify",
    "typescript":["typescript","javascript"],
    "redux":["redux","react"],
    "android":"android",
    "docker":["docker"],
    "matplotlib":["matplotlib","data-visualization"],
    "php":"php",
    "dynamic-programming":["dynamic-programming","algorithm"],
    "interview-questions":["interview-questions","interview"],
    "networking":["networking"],
    "python3":["python3","python"],
    "python 3":["python3","python"],
    "express":["expressjs","javascript","webdev"],
    "expressjs":["expressjs","javascript","webdev"],
    "numpy":["numpy","data-science","lib"],
    "rust":["rust"],
    "rustlang":["rust"],
    "youtube":"youtube"
    
}

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

# docs = get_data()
# KEYWORD_MODEL = create_model(KEYWORD_MODEL_FILE,docs,topics)
KEYWORD_MODEL = load_model(KEYWORD_MODEL_FILE)