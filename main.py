from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from datetime import date


def configuracaoDriver():
    # Caminho do executável do ChromeDriver
    chrome_path = 'C:\Desenvolvimento\workspace\WebScrapEpicGames\chromedriver.exe'

    # Configuração do WebDriver do Chrome
    chrome_service = ChromeService(chrome_path)
    driver_config = webdriver.Chrome(service=chrome_service)

    # URL do site para fazer o Web Scraping
    URL_BASE = "https://store.epicgames.com/en-US/?lang=en-US"

    # Abre a URL no navegador
    driver_config.get(URL_BASE)

    # Encontrar os elementos que contêm os jogos gratuitos
    games = driver_config.find_elements("class name", "css-1ukp34s")

    return driver_config, games


def execucaoPrincipal(div_games):
    with open('games.txt', 'r') as arquivoLeitura:
        jogosLidos = arquivoLeitura.read()

    indexGameStartDate = jogosLidos.rfind('at')
    gameStartDate = jogosLidos[(indexGameStartDate - 7):(indexGameStartDate + 11)]

    ano = date.today().year

    print("Jogos Gratuitos no Momento:")

    with open('games.txt', 'a') as arquivoEscrita:
        for div_game in div_games:
            gameInfos = div_game.text

            startIndex = gameInfos.find('FREE NOW')
            endIndex = gameInfos.find('Free Now')
            gameName = gameInfos[(startIndex + 9):(endIndex - 1)]

            finalDate = gameInfos.rfind('at')
            gameFinalDate = gameInfos[(finalDate - 7):(finalDate + 11)]

            gameArray = [gameName, gameStartDate, gameFinalDate]

            if "Unlocking" not in gameName:
                print(gameName + '\n')

                if gameName not in jogosLidos:
                    formatSave = str(gameArray[0] + "\n   Data de Resgate: " + str(ano) + " " + gameArray[1] + " -> " + str(ano) + " " + gameArray[2] + "\n\n")
                    arquivoEscrita.write(formatSave)

                    print("Adicionando jogo ao arquivo...\n")
                else:
                    print("Jogo já adicionado ao arquivo.\n")
    return


if __name__ == '__main__':
    try:
        driver, divGames = configuracaoDriver()

        execucaoPrincipal(divGames)

        # Fechar o navegador
        driver.quit()

        print("Fim da execução")

    except KeyboardInterrupt:
        print('Saindo do programa...')
