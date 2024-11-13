import uvicorn
from br.adapters import br_starlette

app = br_starlette
if __name__ == "__main__": uvicorn.run(f'server:app', host="0.0.0.0", port=5001)
