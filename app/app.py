import streamlit as st
import aerospike
from aerospike import predicates as p
import google.generativeai as genai
import os, uuid
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-2.5-flash')
# Connect to Aerospike using service name from docker-compose
client = aerospike.client({'hosts': [(os.getenv("AEROSPIKE_HOST"), 3000)]}).connect()

# SETUP: Create Secondary Index if not exists
try:
    client.index_string_create('test', 'recipes', 'island', 'island_idx')
except Exception:
    pass # Index already exists

st.title("🌴 Caribbean AI Kitchen")

# Sidebar Search
islands = ["All", "Jamaica", "Trinidad", "Haiti", "Cuba"]
filter_choice = st.sidebar.selectbox("Filter by Island:", islands)

pantry = st.text_input("Ingredients on hand:")

if st.button("Generate & Save"):
    prompt = f"Expert Caribbean chef: Create a recipe with {pantry}. Start with 'Origin: [Island Name]'."
    res = model.generate_content(prompt).text
    
    # Simple parsing for the index bin
    island_tag = "Jamaica" if "Jamaica" in res else "Trinidad" # Simplified for demo
    
    # Save to Aerospike
    key = ('test', 'recipes', str(uuid.uuid4()))
    client.put(key, {'island': island_tag, 'content': res})
    st.markdown(res)

st.divider()

# Query with Secondary Index
st.subheader(f"Saved {filter_choice} Recipes")
query = client.query('test', 'recipes')
if filter_choice != "All":
    query.where(p.equals('island', filter_choice))

query.foreach(lambda x: st.info(x[2].get('content')))
