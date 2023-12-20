from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

if __name__ == '__main__':
    # Substitua pelo caminho real para o seu executável do ChromeDriver
    chrome_path = 'C:\Desenvolvimento\workspace\WebScrapEpicGames\chromedriver.exe'

    # Configuração do WebDriver do Chrome
    chrome_service = ChromeService(chrome_path)
    driver = webdriver.Chrome(service=chrome_service)

    URL_BASE = "https://store.epicgames.com/en-US/?lang=en-US"

    # Abre a URL no navegador
    driver.get(URL_BASE)

    # Encontrar os elementos que contêm os jogos gratuitos
    freeGames = driver.find_elements("class name", "css-1ukp34s")
    count = len(freeGames)

    with open('games.txt', 'a') as arquivoEscrita:
        for game in freeGames:
            gamesText = game.text

            startIndex = gamesText.find('FREE NOW')
            endIndex = gamesText.find('Free Now')
            name = gamesText[(startIndex + 9):(endIndex - 1)]

            if "Unlocking" not in name:
                print(name)
                with open('games.txt', 'r') as arquivoLeitura:
                    jogosLidos = arquivoLeitura.read()
                    if name not in jogosLidos:
                        arquivoEscrita.write(name + '\n')
                    else:
                        print("Jogo já adicionado")

    # Fechar o navegador
    driver.quit()
