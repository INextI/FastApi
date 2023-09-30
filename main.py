import uvicorn

if __name__ == '__main__':
    uvicorn.run(
        "app:app",
        host='0.0.0.0', #0.0.0.0 #127.0.0.1
        port=10000,    #10000   #8000
        reload=True
    )