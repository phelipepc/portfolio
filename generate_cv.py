#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de CV em PDF - Phelipe Pires Corrêa
AI Engineer & Solutions Architect
"""

from fpdf import FPDF
import os

class CVPDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=25)
        
    def header(self):
        if self.page_no() == 1:
            return
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(120, 120, 120)
        self.cell(0, 5, 'Phelipe Pires Corrêa | AI Engineer & Solutions Architect', align='C')
        self.ln(8)
        self.set_draw_color(0, 212, 170)
        self.set_line_width(0.3)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(5)
    
    def footer(self):
        self.set_y(-20)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(120, 120, 120)
        self.cell(0, 10, f'Pagina {self.page_no()}/{{nb}}', align='C')
    
    def section_title(self, title, icon=""):
        self.set_font('Helvetica', 'B', 13)
        self.set_text_color(0, 212, 170)
        self.cell(0, 10, f'{icon} {title.upper()}', new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(0, 212, 170)
        self.set_line_width(0.5)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(4)
    
    def body_text(self, text):
        self.set_font('Helvetica', '', 10)
        self.set_text_color(40, 40, 40)
        self.multi_cell(0, 5.5, text)
        self.ln(2)
    
    def bullet_point(self, text, indent=15):
        x = self.get_x()
        self.set_font('Helvetica', '', 10)
        self.set_text_color(40, 40, 40)
        self.cell(indent, 5.5, '-')
        self.multi_cell(0, 5.5, text)
        self.ln(1)
    
    def role_header(self, role, company, period, location=""):
        self.set_font('Helvetica', 'B', 11)
        self.set_text_color(20, 20, 20)
        self.cell(0, 6, role, new_x="LMARGIN", new_y="NEXT")
        self.set_font('Helvetica', '', 10)
        self.set_text_color(80, 80, 80)
        info = f'{company}  |  {period}'
        if location:
            info += f'  |  {location}'
        self.cell(0, 5.5, info, new_x="LMARGIN", new_y="NEXT")
        self.ln(1)
    
    def skill_row(self, category, skills):
        self.set_font('Helvetica', 'B', 10)
        self.set_text_color(0, 212, 170)
        self.cell(45, 5.5, category)
        self.set_font('Helvetica', '', 9.5)
        self.set_text_color(40, 40, 40)
        self.multi_cell(0, 5.5, skills)
        self.ln(1.5)


pdf = CVPDF()
pdf.alias_nb_pages()
pdf.add_page()

# ==================== HEADER ====================
pdf.set_font('Helvetica', 'B', 26)
pdf.set_text_color(10, 14, 20)
pdf.cell(0, 12, 'Phelipe Pires Corr\xeaa', new_x="LMARGIN", new_y="NEXT")

pdf.set_font('Helvetica', '', 13)
pdf.set_text_color(0, 212, 170)
pdf.cell(0, 8, 'AI Engineer & Solutions Architect', new_x="LMARGIN", new_y="NEXT")

pdf.ln(2)
pdf.set_draw_color(0, 212, 170)
pdf.set_line_width(0.8)
pdf.line(10, pdf.get_y(), 200, pdf.get_y())
pdf.ln(4)

# Contact info
pdf.set_font('Helvetica', '', 9.5)
pdf.set_text_color(80, 80, 80)
contacts = [
    ('email', 'phelipe.pcorrea@gmail.com'),
    ('phone', '+55 27 99603-0550'),
    ('location', 'Serra, ES - Brasil'),
    ('linkedin', 'linkedin.com/in/phelipe-correa'),
    ('github', 'github.com/phelipepc'),
]
contact_str = '   |   '.join([c[1] for c in contacts])
pdf.cell(0, 5.5, contact_str, new_x="LMARGIN", new_y="NEXT", align='C')
pdf.ln(6)

# ==================== SUMMARY (PAS) ====================
pdf.section_title('Resumo Profissional', '>>')

summary = (
    "PROBLEMA: Empresas lutam para transformar dados complexos em produtos de IA escalaveis, "
    "enfrentando gargalos de concorrencia, latencia e falta de observabilidade em sistemas multiagentes.\n\n"
    "AGITACAO: A maioria das solucoes falha em producao por ausencia de RAG validado, circuit breakers, "
    "execucao isolada de codigo e feedback loops humanos - resultando em alucinacoes, timeouts e custo imprevisivel.\n\n"
    "SOLUCAO: Arquiteturo sistemas de IA generativa resilientes usando CrewAI + LangGraph, RAG avancado "
    "(pgvector/ChromaDB/reranking), Service Bus para load leveling, semaforos distribuidos e observabilidade "
    "nativa (OpenTelemetry/OpenLIT/Grafana). Entreguei 15+ produtos em producao processando 50k+ msg/s "
    "com latencia <50ms p99, reduzindo custos de inferencia em 40% via roteamento inteligente multi-cloud.\n\n"
    "CTA: Aberto a oportunidades de AI Engineering, Solutions Architecture e consultoria tecnica em IA Generativa. "
    "Vamos conversar? phelipe.pcorrea@gmail.com"
)
pdf.body_text(summary)

# ==================== EXPERIENCE (XYZ) ====================
pdf.section_title('Experiencia Profissional', '>>')

# MedSenior
pdf.role_header(
    'Desenvolvedor Python / AI Engineer',
    'MedSenior - Operadora de Saude',
    'jun/2025 - Presente',
    'Serra, ES (Hibrido)'
)

achievements_med = [
    "Alcancei plataforma multiagentes para analytics assistencial (chat-to-SQL + RAG validado) por meio de arquitetura CrewAI + LangGraph com execucao isolada DuckDB/PyArrow, resultando em analise conversacional de autorizacoes, custos e glosas usada por auditoria e diretoria regional.",
    "Alcancei pipeline chat-to-SQL com RAG validado por meio de classificacao de intencao + busca em catalogos TUSS/schema + geracao SQL + validacao EXPLAIN + execucao isolada, resultando em narrativas + graficos automaticos para decisoes de negociacao contratual.",
    "Alcancei analise integrada via LangGraph por meio de grafo de decisao que roteia perguntas para modulos especializados (Autorizacao, Custos, Integrada) em paralelo/sequencial, resultando em roteamento baseado em skills + schema + catalogos (nao apenas keywords).",
    "Alcancei feedback loop humano automatizado por meio de fila de revisao -> correcao SQL -> validacao EXPLAIN -> reindexacao automatica ChromaDB, resultando em melhoria continua de precisao para consultas similares.",
    "Alcancei observabilidade completa por meio de OpenTelemetry + OpenLIT (traces por request, step do grafo, LLM calls) + Grafana dashboards + alertas Teams, resultando em visibilidade total de latencia, tokens, custo e qualidade de resposta.",
    "Alcancei integracao multi-cloud STT por meio de API agnostica (GCP, Azure, OpenAI, Deepgram) com Service Bus para load leveling, resultando em transricao batch/streaming via WebSockets com fallback automatico."
]

for a in achievements_med:
    pdf.bullet_point(a)

pdf.ln(3)

# EL Producoes
pdf.role_header(
    'Desenvolvedor Python / Backend & IA',
    'EL Producoes de Software',
    'set/2022 - jun/2025',
    'Vitoria, ES'
)

achievements_el = [
    "Alcancei 10+ aplicacoes com integracao LLMs por meio de Python + LangChain + OpenAI GPT, resultando em automacao de processos cognitivos e reducao de 60% esforco manual.",
    "Alcancei pipelines ETL robustas por meio de Pentaho + SAS Viya + Metabase, resultando em dashboards interativos para tomada de decisao executiva.",
    "Alcancei modelagem de dados enterprise por meio de Oracle/MySQL/PostgreSQL (triggers, views, procedures), resultando em integridade e performance em alto volume.",
    "Alcancei APIs REST para integracao de sistemas por meio de Docker + Python, resultando em ambientes de dev padronizados e deploy consistente.",
    "Alcancei migracao Java/JSF (Primefaces) para stack Python por meio de refatoracao gradual, resultando em modernizacao tecnologica e reducao de debt tecnico."
]

for a in achievements_el:
    pdf.bullet_point(a)

pdf.ln(3)

# Giro
pdf.role_header(
    'Desenvolvedor Python / Full Stack',
    'Giro',
    'abr/2020 - jul/2022',
    'Vitoria, ES'
)

achievements_giro = [
    "Alcancei 15+ automacoes e aplicacoes web por meio de Python (Pandas, Selenium, Tkinter, Django), resultando em ganhos de eficiencia operacional para clientes B2B.",
    "Alcancei ferramentas CRUD e dashboards por meio de MySQL/SQLite/PostgreSQL + Python Dash, resultando em visibilidade de dados em tempo real.",
    "Alcancei infraestrutura cloud AWS por meio de RDS, EC2, Lightsail, Nginx + deploy Django, resultando em ambientes escalaveis e custo otimizado.",
    "Alcancei extracao e integracao de dados por meio de Selenium + Requests, resultando em pipelines de dados automatizadas de fontes externas."
]

for a in achievements_giro:
    pdf.bullet_point(a)

pdf.ln(3)

# Formacao Juridica
pdf.role_header(
    'Formacao Juridica & Pratica Advocaticia',
    'TJES (Estagiario) -> Siqueira Castro Advogados',
    '2013 - 2018',
    'Vitoria, ES'
)

achievements_law = [
    "Conclui Bacharelado em Direito (2011-2015) + Pos-graduacao Direito Tributario (2016-2017), desenvolvendo rigor analitico, redacao tecnica, compliance e analise de risco - base para arquitetura de software resiliente.",
    "Atuei em Direito Civil, Empresarial e LGPD - contratos, compliance, protecao de dados, estruturacao de startups (societario, PI, termos de uso, politicas)."
]

for a in achievements_law:
    pdf.bullet_point(a)

# ==================== KEY PROJECTS ====================
pdf.section_title('Projetos Principais (Deployments em Producao)', '>>')

projects = [
    ("Plataforma Analytics Conversacional Saude (MedSenior)",
     "Chat-to-SQL com RAG validado (pgvector/ChromaDB) + execucao isolada DuckDB/PyArrow + Delta Sharing (Databricks) + LangGraph routing + feedback loop humano + OpenTelemetry/OpenLIT. Usado por auditoria, controladoria, diretoria regional.",
     "Python, FastAPI, CrewAI, LangGraph, LangChain, LiteLLM, DuckDB, PyArrow, Delta Sharing, Databricks, PostgreSQL, pgvector, ChromaDB, Keycloak, OpenTelemetry, OpenLIT, Grafana, Docker, Azure DevOps, WebSockets, Service Bus"),
    
    ("Ecossistema Multiagentes Compliance & Marketing",
     "Agentes autonomos (CrewAI) para validacao, auditoria, classificacao de transcricoes/PDFs + cronjobs autonomos + PostgreSQL/Alembic. Pipeline 100% automatizado sem intervencao humana.",
     "Python, CrewAI, FastAPI, PostgreSQL, Alembic, Cron/APScheduler, Docker"),
    
    ("Chatbot B2C WhatsApp com RAG (Llama/GroqCloud)",
     "RAG sobre catalogo produtos (embeddings + pgvector) + Llama via GroqCloud + EvolutionAPI WhatsApp Business + consulta tempo real banco relacional (estoque, preco, specs).",
     "Python, Llama, GroqCloud, EvolutionAPI, pgvector, PostgreSQL, Docker"),
    
    ("API Transcricao Agnostica Multi-cloud",
     "API unificada (GCP Speech, Azure Speech, OpenAI Whisper, Deepgram) + Batch/Streaming WebSockets + roteamento inteligente custo/latencia/qualidade + Service Bus + semaforos concorrencia.",
     "Python, FastAPI, WebSockets, Service Bus, GCP, Azure, OpenAI, Deepgram, Docker"),
    
    ("Refatoracao Concorrencia - Sistema Mais/DAC",
     "Eliminacao travamentos sistemicos via Service Bus (load leveling) + semaforos distribuidos. Erradicacao race conditions/deadlocks. Throughput 3x+ sob pico.",
     "Python, Service Bus, Semaforos, AsyncIO, Docker"),
    
    ("Motor Busca Vetorial Auditoria Medica (TUSS)",
     "RAG sobre avaliacoes saude + tabela TUSS (pgvector + OpenAI embeddings + RapidFuzz) + saida JSON estruturada. Aceleracao significativa auditoria medica.",
     "Python, pgvector, OpenAI, PostgreSQL, RapidFuzz, TUSS, Docker"),
]

for title, desc, stack in projects:
    pdf.set_font('Helvetica', 'B', 10.5)
    pdf.set_text_color(20, 20, 20)
    pdf.cell(0, 6, title, new_x="LMARGIN", new_y="NEXT")
    pdf.set_font('Helvetica', '', 9.5)
    pdf.set_text_color(50, 50, 50)
    pdf.multi_cell(0, 5, desc)
    pdf.ln(1)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_text_color(0, 212, 170)
    pdf.cell(25, 5, 'Stack: ')
    pdf.set_font('Helvetica', '', 8.5)
    pdf.set_text_color(80, 80, 80)
    pdf.multi_cell(0, 5, stack)
    pdf.ln(4)

# ==================== TECHNICAL SKILLS ====================
pdf.section_title('Competencias Tecnicas', '>>')

skills = [
    ("IA Generativa & Multiagentes", "CrewAI, LangGraph, LangChain, AutoGen, OpenAI API, Anthropic API, Prompt Engineering, Function Calling, Agentic Workflows, RAG (pgvector, ChromaDB, Pinecone), Reranking, Hybrid Search, Embeddings, Chunking Strategies"),
    ("Backend & APIs", "Python 3.11-3.13, FastAPI, Pydantic v2, SQLAlchemy, AsyncIO, WebSockets, GraphQL, REST, Service Bus, Mensageria, Dependency Injection, CopilotKit, AG-UI"),
    ("Dados & Infraestrutura", "PostgreSQL, pgvector, DuckDB, PyArrow, Delta Sharing, Databricks, Redis, Docker, Docker Compose, Kubernetes (EKS/GKE), Terraform (basico), Nginx, AWS (RDS, EC2, Lambda), GCP, Azure"),
    ("Observabilidade & Resiliencia", "OpenTelemetry, OpenLIT, Grafana, Loki, Prometheus, Distributed Tracing, Circuit Breaker, Rate Limiting, Retry Logic, Semaforos Distribuidos, SLO/SLI, Day-2 Operations, Cost Tracking"),
    ("Engenharia & Praticas", "Clean Architecture, DDD, TDD, CI/CD, GitOps, Microservices, Event-Driven, SOLID, Alembic Migrations, pytest, Ruff, mypy, Azure DevOps"),
]

for cat, sk in skills:
    pdf.skill_row(cat, sk)

# ==================== EDUCATION ====================
pdf.section_title('Formacao Academica', '>>')

pdf.set_font('Helvetica', 'B', 10.5)
pdf.set_text_color(20, 20, 20)
pdf.cell(0, 6, 'Pos-graduacao em Arquitetura de Software', new_x="LMARGIN", new_y="NEXT")
pdf.set_font('Helvetica', '', 10)
pdf.set_text_color(80, 80, 80)
pdf.cell(0, 5.5, 'UNOPAR - Universidade Norte do Parana  |  jun/2023 - dez/2023', new_x="LMARGIN", new_y="NEXT")
pdf.ln(2)

pdf.set_font('Helvetica', 'B', 10.5)
pdf.set_text_color(20, 20, 20)
pdf.cell(0, 6, 'Pos-graduacao em Direito e Processo Tributario', new_x="LMARGIN", new_y="NEXT")
pdf.set_font('Helvetica', '', 10)
pdf.set_text_color(80, 80, 80)
pdf.cell(0, 5.5, 'FDV - Faculdade de Direito de Vitoria  |  2016 - 2017', new_x="LMARGIN", new_y="NEXT")
pdf.ln(2)

pdf.set_font('Helvetica', 'B', 10.5)
pdf.set_text_color(20, 20, 20)
pdf.cell(0, 6, 'Bacharelado em Direito', new_x="LMARGIN", new_y="NEXT")
pdf.set_font('Helvetica', '', 10)
pdf.set_text_color(80, 80, 80)
pdf.cell(0, 5.5, 'Rede de Ensino Doctum  |  2011 - 2015', new_x="LMARGIN", new_y="NEXT")
pdf.ln(4)

# ==================== CERTIFICATIONS ====================
pdf.section_title('Certificacoes & Aprendizado Continuo', '>>')

certs = [
    "SQL Server, MySQL, Oracle, T-SQL, PL/SQL",
    "Python Web (Django), Java OOP",
    "Pentaho / ETL, PostgreSQL",
    "AWS / GCP / Azure Fundamentals",
    "Docker, Kubernetes Basics",
    "LangChain, LangGraph, CrewAI (autoestudo avancado)",
    "OpenTelemetry, Grafana, Prometheus (observabilidade pratica)",
]

for c in certs:
    pdf.bullet_point(c, indent=10)

pdf.ln(3)

# ==================== FOOTER NOTE ====================
pdf.set_draw_color(0, 212, 170)
pdf.set_line_width(0.3)
pdf.line(10, pdf.get_y(), 200, pdf.get_y())
pdf.ln(3)
pdf.set_font('Helvetica', 'I', 9)
pdf.set_text_color(100, 100, 100)
pdf.multi_cell(0, 5, 
    'Portfolio: https://phelipepc.github.io/portfolio/  |  '
    'GitHub: github.com/phelipepc  |  '
    'LinkedIn: linkedin.com/in/phelipe-correa  |  '
    'Disponivel para: AI Engineering, Solutions Architecture, Consultoria Tecnica, Projetos IA Generativa'
)

# Save
output_path = 'C:/Users/pheli/portfolio-site/Phelipe_Pires_Correa_CV.pdf'
pdf.output(output_path)
print(f'PDF gerado: {output_path}')
print(f'Paginas: {pdf.page_no()}')