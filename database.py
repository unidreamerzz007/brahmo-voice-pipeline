import sqlite3
import os
import json

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pipeline.db")

def get_connection():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    # Enable foreign keys
    cursor.execute("PRAGMA foreign_keys = ON;")
    
    # 1. medical_dictionary table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS medical_dictionary (
        term TEXT PRIMARY KEY,
        term_type TEXT NOT NULL,
        phonetic TEXT,
        common_mistranscriptions TEXT, -- JSON array of strings
        brand_names TEXT -- JSON array of strings
    );
    """)

    # 2. knowledge_nodes table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS knowledge_nodes (
        id TEXT PRIMARY KEY,
        org_id TEXT NOT NULL DEFAULT 'supra',
        type TEXT NOT NULL CHECK (type IN ('CONSTRAINT', 'DECISION', 'ANTI_PATTERN', 'FACT')),
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        importance DECIMAL(3,2) NOT NULL,
        department TEXT,
        hierarchy_level INTEGER,
        source TEXT DEFAULT 'VOICE_CAPTURE',
        source_transcript_id TEXT,
        created_by TEXT NOT NULL,
        created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # 3. transcripts table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transcripts (
        id TEXT PRIMARY KEY,
        doctor_id TEXT NOT NULL,
        patient_id TEXT,
        language_code TEXT NOT NULL,
        asr_provider TEXT NOT NULL,
        asr_provider_reason TEXT,
        raw_transcript TEXT NOT NULL,
        corrected_transcript TEXT,
        confirmed_transcript TEXT,
        corrections_applied TEXT, -- JSON object
        segments TEXT, -- JSON array
        overall_confidence DECIMAL(3,2),
        status TEXT DEFAULT 'PENDING',
        pipeline_time_ms INTEGER,
        confirmed_at TIMESTAMPTZ,
        created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # 4. asr_evaluations table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS asr_evaluations (
        id TEXT PRIMARY KEY,
        provider_name TEXT NOT NULL,
        provider_type TEXT NOT NULL,
        description TEXT,
        languages_supported TEXT, -- JSON array
        code_switch_support TEXT CHECK (code_switch_support IN ('native', 'workaround', 'none')),
        cost_per_hour DECIMAL(10,2),
        cost_currency TEXT DEFAULT 'INR',
        latency_seconds DECIMAL(5,2),
        privacy_model TEXT,
        wer_overall DECIMAL(5,2),
        wer_by_language TEXT, -- JSON object
        medical_term_accuracy DECIMAL(5,2),
        negation_accuracy DECIMAL(5,2),
        chosen BOOLEAN DEFAULT 0,
        chosen_reason TEXT,
        rejected_reason TEXT,
        test_date TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # 5. accuracy_results table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS accuracy_results (
        id TEXT PRIMARY KEY,
        voice_note_id TEXT NOT NULL,
        language TEXT NOT NULL,
        specialty TEXT NOT NULL,
        your_provider TEXT NOT NULL,
        your_transcript TEXT,
        your_wer DECIMAL(5,2),
        your_medical_term_accuracy DECIMAL(5,2),
        your_negation_preserved BOOLEAN,
        your_nodes_extracted TEXT, -- JSON array
        your_node_count INTEGER,
        your_node_accuracy DECIMAL(5,2),
        chatgpt_output TEXT,
        chatgpt_nodes TEXT, -- JSON array
        chatgpt_node_accuracy DECIMAL(5,2),
        baseline2_name TEXT,
        baseline2_output TEXT,
        baseline2_node_accuracy DECIMAL(5,2),
        danger_level TEXT CHECK (danger_level IN ('SAFE', 'MODERATE', 'CRITICAL')),
        negation_critical BOOLEAN DEFAULT 0,
        generic_ai_dangerous BOOLEAN DEFAULT 0,
        notes TEXT,
        tested_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # 6. cost_analysis table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cost_analysis (
        id TEXT PRIMARY KEY,
        provider TEXT NOT NULL,
        scenario TEXT NOT NULL,
        doctors_count INTEGER NOT NULL,
        notes_per_day INTEGER NOT NULL,
        seconds_per_note INTEGER DEFAULT 30,
        daily_hours DECIMAL(5,2),
        monthly_cost DECIMAL(10,2),
        annual_cost DECIMAL(12,2),
        cost_per_node DECIMAL(5,2),
        currency TEXT DEFAULT 'INR',
        notes TEXT,
        created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
    );
    """)

    conn.commit()
    conn.close()
    print("Database initialized successfully.")

if __name__ == "__main__":
    init_db()
