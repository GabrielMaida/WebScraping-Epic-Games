from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


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
    with open('games.txt', 'a') as arquivoEscrita:
        for game in div_games:
            gameInfos = game.text

            startIndex = gameInfos.find('FREE NOW')
            endIndex = gameInfos.find('Free Now')
            gameName = gameInfos[(startIndex + 9):(endIndex - 1)]

            indexDate = gameInfos.rfind('at')
            gameDate = gameInfos[(indexDate - 7):(indexDate + 11)]

            if "Unlocking" not in gameName:
                print("Jogos Gratuitos\n" + gameName + '\n')

                with open('games.txt', 'r') as arquivoLeitura:
                    jogosLidos = arquivoLeitura.read()

                    if gameName not in jogosLidos:
                        arquivoEscrita.write(gameName + ' - ' + gameDate + '\n')
                        print("Jogo adicionado.")
                    else:
                        print("Jogo já adicionado.")
    return


if __name__ == '__main__':
    driver, divGames = configuracaoDriver()

    execucaoPrincipal(divGames)

    # Fechar o navegador
    driver.quit()
