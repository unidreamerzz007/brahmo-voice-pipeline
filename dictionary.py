import json

# Top drugs, dosage units, and labs with brand names and common ASR mistranscriptions
DRUG_DICTIONARY = [
    # Top drugs
    {
        "term": "Paracetamol", "term_type": "drug", "phonetic": "pa-ra-SEE-ta-mol",
        "common_mistranscriptions": ["parasitamol", "para see tamol", "paris at a mall", "para sita mole", "paracetamol"],
        "brand_names": ["Calpol", "Dolo", "Crocin", "Tylenol", "P-650"]
    },
    {
        "term": "Ibuprofen", "term_type": "drug", "phonetic": "eye-bew-PRO-fen",
        "common_mistranscriptions": ["I be proven", "ibu pro fan", "I view profen", "I proof in", "ibuprofen"],
        "brand_names": ["Brufen", "Combiflam", "Advil", "Ibugesic"]
    },
    {
        "term": "Tramadol", "term_type": "drug", "phonetic": "TRA-ma-dol",
        "common_mistranscriptions": ["trauma doll", "tram a doll", "trauma dull", "tramadole", "tramadol"],
        "brand_names": ["Ultracet", "Contramal", "Tramatas"]
    },
    {
        "term": "Metformin", "term_type": "drug", "phonetic": "met-FOR-min",
        "common_mistranscriptions": ["met for men", "metaphor min", "met forming", "metform in", "metformin"],
        "brand_names": ["Glycomet", "Glucophage", "Obimet", "Gluformin"]
    },
    {
        "term": "Glimepiride", "term_type": "drug", "phonetic": "glim-EP-i-ride",
        "common_mistranscriptions": ["glimpse ride", "glib pride", "glam a pride", "glimmer ride", "glimepiride"],
        "brand_names": ["Amaryl", "Glimstar", "Glimy"]
    },
    {
        "term": "Warfarin", "term_type": "drug", "phonetic": "WAR-fa-rin",
        "common_mistranscriptions": ["war for in", "warfare in", "war faring", "wore far in", "warfarin"],
        "brand_names": ["Coumadin", "Warf", "Sofarin"]
    },
    {
        "term": "Clopidogrel", "term_type": "drug", "phonetic": "klo-PID-o-grel",
        "common_mistranscriptions": ["close pedigree", "clopidol grill", "club piddle grill", "clopidogrel"],
        "brand_names": ["Plavix", "Clopilet", "Deplatt", "Clopivas"]
    },
    {
        "term": "Enoxaparin", "term_type": "drug", "phonetic": "en-OX-a-pa-rin",
        "common_mistranscriptions": ["e nox a parr in", "enox a parent", "in ox a paring", "enoxaparin"],
        "brand_names": ["Clexane", "Lovenox", "Lmwx"]
    },
    {
        "term": "Aspirin", "term_type": "drug", "phonetic": "AS-pir-in",
        "common_mistranscriptions": ["aspiring", "a spring", "as per in", "aspren", "aspirin"],
        "brand_names": ["Ecosprin", "Disprin", "Loprin"]
    },
    {
        "term": "Atorvastatin", "term_type": "drug", "phonetic": "a-TOR-va-sta-tin",
        "common_mistranscriptions": ["a tour of statin", "at or vast a tin", "at over statin", "atorvastatin"],
        "brand_names": ["Atorva", "Lipitor", "Tonact", "Storvas"]
    },
    {
        "term": "Omeprazole", "term_type": "drug", "phonetic": "oh-MEP-ra-zol",
        "common_mistranscriptions": ["oh my prays all", "home a prism", "omega prazoal", "omeprazole"],
        "brand_names": ["Omez", "Prilosec", "Ocid"]
    },
    {
        "term": "Pantoprazole", "term_type": "drug", "phonetic": "pan-TOE-pra-zol",
        "common_mistranscriptions": ["pant oh pray soul", "panther prays all", "panto prism", "pantoprazole"],
        "brand_names": ["Pan 40", "Pantocid", "Nexpro", "Pantop"]
    },
    {
        "term": "Amoxicillin", "term_type": "drug", "phonetic": "a-MOX-i-sil-in",
        "common_mistranscriptions": ["a moxie see lin", "amoks see lin", "a mock silly in", "amoxicillin"],
        "brand_names": ["Mox", "Amoxil", "Novamox", "Moxylong"]
    },
    {
        "term": "Azithromycin", "term_type": "drug", "phonetic": "a-ZITH-ro-my-sin",
        "common_mistranscriptions": ["a with row my sin", "az throw my sin", "a zither oh my sin", "azithromycin"],
        "brand_names": ["Azithral", "Zithromax", "Azee", "Azikem"]
    },
    {
        "term": "Telmisartan", "term_type": "drug", "phonetic": "tel-mi-SAR-tan",
        "common_mistranscriptions": ["tell me sartan", "tele me start on", "telma sartan", "telmisartan"],
        "brand_names": ["Telma", "Micardis", "Telmikind", "Sartel"]
    },
    {
        "term": "Amlodipine", "term_type": "drug", "phonetic": "am-LOD-i-peen",
        "common_mistranscriptions": ["am loading peen", "amlo di pine", "a melody pin", "amlodipine"],
        "brand_names": ["Amlodac", "Norvasc", "Amlopress", "Amlokind"]
    },
    {
        "term": "Metoprolol", "term_type": "drug", "phonetic": "me-TOE-pro-lol",
        "common_mistranscriptions": ["metal oil", "met oh pro lol", "me toe pro loll", "metoprolol"],
        "brand_names": ["Metolar", "Betaloc", "Lopressor", "Seloken"]
    },
    {
        "term": "Ramipril", "term_type": "drug", "phonetic": "RAM-i-pril",
        "common_mistranscriptions": ["ram a pill", "ramp aril", "rami prill", "ramipril"],
        "brand_names": ["Cardace", "Ramistar", "Ramace"]
    },
    {
        "term": "Escitalopram", "term_type": "drug", "phonetic": "es-si-TAL-o-pram",
        "common_mistranscriptions": ["escape tell a pram", "es sit a low pram", "es cital o pram", "escitalopram"],
        "brand_names": ["Nexito", "Cipralex", "Lexapro", "S-Citadep"]
    },
    {
        "term": "Levothyroxine", "term_type": "drug", "phonetic": "lee-vo-thy-ROX-een",
        "common_mistranscriptions": ["leave oh thy rocks in", "levo thigh roxanne", "levothyroxine"],
        "brand_names": ["Thyronorm", "Eltroxin", "Synthroid", "Lethyrox"]
    },
    {
        "term": "Prednisolone", "term_type": "drug", "phonetic": "pred-NIS-o-lone",
        "common_mistranscriptions": ["predator so lone", "pred ni solo", "prednisone alone", "prednisolone"],
        "brand_names": ["Wysolone", "Omnacortil"]
    },
    {
        "term": "Methylprednisolone", "term_type": "drug", "phonetic": "meth-il-pred-NIS-o-lone",
        "common_mistranscriptions": ["methyl predator so lone", "metal prednisone", "methylprednisolone"],
        "brand_names": ["Medrol", "Solumedrol"]
    },
    {
        "term": "Furosemide", "term_type": "drug", "phonetic": "few-ROSE-a-mide",
        "common_mistranscriptions": ["furious a maid", "few rows a mid", "furose might", "furosemide"],
        "brand_names": ["Lasix", "Frusenex", "Frusemide"]
    },
    {
        "term": "Spironolactone", "term_type": "drug", "phonetic": "spy-ro-no-LAK-tone",
        "common_mistranscriptions": ["spiral lactone", "spy rono lack tone", "spironolactone"],
        "brand_names": ["Aldactone", "Spirotone"]
    },
    {
        "term": "Torsemide", "term_type": "drug", "phonetic": "TOR-se-mide",
        "common_mistranscriptions": ["tour semi day", "toss a mide", "torso might", "torsemide"],
        "brand_names": ["Dytor", "Demadex", "Tide"]
    },
    {
        "term": "Insulin Glargine", "term_type": "drug", "phonetic": "IN-su-lin GLAR-jeen",
        "common_mistranscriptions": ["insult in glarjeen", "insulin glad gene", "insulin glargine"],
        "brand_names": ["Lantus", "Basalog", "Glaritus"]
    },
    {
        "term": "Insulin Aspart", "term_type": "drug", "phonetic": "IN-su-lin AS-part",
        "common_mistranscriptions": ["insult in apart", "insulin as part", "insulin aspart"],
        "brand_names": ["Novorapid", "Fiasp"]
    },
    {
        "term": "Clarithromycin", "term_type": "drug", "phonetic": "kla-RITH-ro-my-sin",
        "common_mistranscriptions": ["clarity row my sin", "cla rhythm ice in", "clarithromycin"],
        "brand_names": ["Klaricid", "Claribid", "Klacid"]
    },
    {
        "term": "Cefuroxime", "term_type": "drug", "phonetic": "sef-yoo-ROX-eem",
        "common_mistranscriptions": ["safe you rocks him", "sef euro extreme", "cefuroxime"],
        "brand_names": ["Ceftum", "Zinacef", "Supacef"]
    },
    {
        "term": "Apixaban", "term_type": "drug", "phonetic": "a-PIX-a-ban",
        "common_mistranscriptions": ["a picks a ban", "apex a ban", "a pixel ban", "apixaban"],
        "brand_names": ["Eliquis", "Apigat"]
    },
    {
        "term": "Linagliptin", "term_type": "drug", "phonetic": "lin-a-GLIP-tin",
        "common_mistranscriptions": ["linear glip tin", "lina grip tin", "linagliptin"],
        "brand_names": ["Trajenta", "Linage"]
    },
    {
        "term": "Labetalol", "term_type": "drug", "phonetic": "la-BET-a-lol",
        "common_mistranscriptions": ["label all", "la better lol", "label a lol", "labetalol"],
        "brand_names": ["Lobet", "Normodyne"]
    },
    {
        "term": "Hydroxychloroquine", "term_type": "drug", "phonetic": "hy-drox-ee-KLOR-o-kween",
        "common_mistranscriptions": ["hydroxy chloroquine", "hydroxy claw queen", "hydroxychloroquine"],
        "brand_names": ["HCQS", "Plaquenil"]
    },
    {
        "term": "Methotrexate", "term_type": "drug", "phonetic": "meth-oh-TREX-ate",
        "common_mistranscriptions": ["metro tracks eight", "method tracks ate", "methotrexate"],
        "brand_names": ["Folitrax", "Imutrex"]
    },
    {
        "term": "Gabapentin", "term_type": "drug", "phonetic": "gab-a-PEN-tin",
        "common_mistranscriptions": ["grab a pen tin", "gab upon tin", "gabapentin"],
        "brand_names": ["Gabapin", "Neurontin", "Gabatop"]
    },
    
    # Dosage units
    {"term": "QDS", "term_type": "dosage_unit", "phonetic": "Q-D-S", "common_mistranscriptions": ["cue d s", "kudos", "cuties", "qds"], "brand_names": []},
    {"term": "TDS", "term_type": "dosage_unit", "phonetic": "T-D-S", "common_mistranscriptions": ["t d s", "tedious", "teddies", "tds"], "brand_names": []},
    {"term": "BD", "term_type": "dosage_unit", "phonetic": "B-D", "common_mistranscriptions": ["be de", "beady", "buddy", "bd"], "brand_names": []},
    {"term": "OD", "term_type": "dosage_unit", "phonetic": "O-D", "common_mistranscriptions": ["oh dee", "ode", "oddy", "od"], "brand_names": []},
    {"term": "PRN", "term_type": "dosage_unit", "phonetic": "P-R-N", "common_mistranscriptions": ["pee are en", "pirn", "preen", "prn"], "brand_names": []},
    {"term": "SOS", "term_type": "dosage_unit", "phonetic": "S-O-S", "common_mistranscriptions": ["sos", "sauce"], "brand_names": []},
    {"term": "STAT", "term_type": "dosage_unit", "phonetic": "STAT", "common_mistranscriptions": ["state", "start", "stat"], "brand_names": []},
    {"term": "HS", "term_type": "dosage_unit", "phonetic": "H-S", "common_mistranscriptions": ["aitch es", "hes", "his", "hs"], "brand_names": []},

    # Lab tests
    {"term": "Troponin", "term_type": "lab_test", "phonetic": "TRO-po-nin", "common_mistranscriptions": ["trope on in", "tropo nine", "tropical nin", "trophy nin", "troponin"], "brand_names": []},
    {"term": "Creatinine", "term_type": "lab_test", "phonetic": "kree-AT-i-neen", "common_mistranscriptions": ["creative nine", "create a nine", "cree atinine", "creatinine"], "brand_names": []},
    {"term": "HbA1c", "term_type": "lab_test", "phonetic": "H-B-A-one-C", "common_mistranscriptions": ["hba one see", "hab a one see", "h b a 1 c", "hba1c"], "brand_names": []},
    {"term": "PT-INR", "term_type": "lab_test", "phonetic": "P-T-I-N-R", "common_mistranscriptions": ["pt inner", "pity inner", "petty in r", "pt-inr"], "brand_names": []}
]

# Negation patterns in various Indian languages and their English equivalents
NEGATION_PATTERNS = {
  "te": {
    "negations": ["ivvaledu", "ivvakudadu", "kudadu", "ledu", "vaddhu", "cheyakandi", "aapandi", "cheyakudadu", "ivvakandi", "vadda", "nillisbekku"],
    "examples": {
      "ivvaledu": "don't give / didn't give",
      "ivvakudadu": "must not give",
      "kudadu": "must not / should not",
      "vaddhu": "don't want",
      "cheyakandi": "don't do",
      "aapandi": "stop it",
      "ivvakandi": "don't give",
      "vadda": "don't want"
    }
  },
  "hi": {
    "negations": ["mat do", "nahi", "band karo", "mat karo", "na dena", "nahi dena", "mat dena", "rok do", "hatao", "bilkul nahi", "mat"],
    "examples": {
      "mat do": "don't give",
      "band karo": "stop / discontinue",
      "nahi dena": "don't give",
      "hatao": "remove",
      "bilkul nahi": "absolutely not"
    }
  },
  "ta": {
    "negations": ["kudadhu", "venda", "illai", "kudaadhu", "pannakudadhu", "kodukka kudadhu", "vaenda", "kudukka kudadhu", "venam", "pannathinga"],
    "examples": {
      "kudadhu": "must not",
      "venda": "don't want / don't need",
      "kodukka kudadhu": "must not give",
      "kudukka kudadhu": "must not give",
      "venam": "don't want / no need"
    }
  },
  "kn": {
    "negations": ["baralla", "kudadu", "beda", "kodabaradu", "maadabaradu", "nillisi", "nillisbekku", "moodlu", "nillisa"],
    "examples": {
      "baralla": "can't / shouldn't",
      "beda": "don't want",
      "kodabaradu": "must not give",
      "nillisi": "stop",
      "nillisbekku": "must stop"
    }
  },
  "ml": {
    "negations": ["paadilla", "aruthhu", "venda", "kodukkaruthhu", "cheyyaruthhu", "kazhikkan paadilla"],
    "examples": {
      "paadilla": "must not / not allowed",
      "aruthhu": "should not",
      "venda": "don't need",
      "kodukkaruthhu": "should not give"
    }
  },
  "mr": {
    "negations": ["deu naka", "nahi", "nako", "band kara", "thambav", "deu naye", "yet navhta"],
    "examples": {
      "deu naka": "don't give",
      "band kara": "stop",
      "nako": "don't want",
      "yet navhta": "was not able to"
    }
  },
  "bn": {
    "negations": ["deben na", "korben na", "bandho korun", "na", "deoaa uchhit noy", "raaji non", "nei"],
    "examples": {
      "deben na": "don't give",
      "korben na": "don't do",
      "bandho korun": "stop / discontinue",
      "raaji non": "not agreeing",
      "nei": "no / doesn't have"
    }
  },
  "gu": {
    "negations": ["aapvo nahi", "nathi", "band karo", "nakko", "na aapo", "nathi lagana", "na lagana"],
    "examples": {
      "aapvo nahi": "don't give",
      "band karo": "stop",
      "nathi": "not / no",
      "na aapo": "don't give"
    }
  }
}

# Mapping of regional number words to numbers
REGIONAL_NUMBERS = {
  "te": {"oka": 1, "rendu": 2, "moodu": 3, "naalugu": 4, "aidu": 5, "aaru": 6, "edu": 7, "enimidi": 8, "thommidi": 9, "padhi": 10, "iravai": 20, "nooru": 100},
  "hi": {"ek": 1, "do": 2, "teen": 3, "chaar": 4, "paanch": 5, "chhe": 6, "saat": 7, "aath": 8, "nau": 9, "das": 10, "bees": 20, "sau": 100, "dedh": 1.5, "dhai": 2.5},
  "ta": {"onnu": 1, "rendu": 2, "moonu": 3, "naalu": 4, "anju": 5, "aaru": 6, "ezhu": 7, "ettu": 8, "onpathu": 9, "pathu": 10, "iruvathu": 20, "nooru": 100},
  "kn": {"ondu": 1, "eradu": 2, "mooru": 3, "nalku": 4, "aidu": 5, "aaru": 6, "elu": 7, "entu": 8, "ombattu": 9, "hathu": 10, "ippathu": 20, "nooru": 100},
  "ml": {"onnu": 1, "randu": 2, "moonnu": 3, "naalu": 4, "anchu": 5, "aaru": 6, "ezhu": 7, "ettu": 8, "onpathu": 9, "pathu": 10},
  "mr": {"ek": 1, "don": 2, "teen": 3, "chaar": 4, "paach": 5, "saha": 6, "saat": 7, "aath": 8, "nau": 9, "daha": 10, "vees": 20},
  "bn": {"ek": 1, "dui": 2, "tin": 3, "char": 4, "panch": 5, "chhoy": 6, "shaat": 7, "aat": 8, "noy": 9, "dosh": 10}
}
