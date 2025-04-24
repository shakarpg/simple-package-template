from PIL import Image

def show_image2(image_path):
    """
    Função para carregar e exibir uma imagem.
    :param image_path: Caminho completo para o arquivo de imagem.
    """
    try:
        # Carregar a imagem
        image = Image.open(image_path)

        # Exibir a imagem
        image.show()
    except FileNotFoundError:
        print(f"Erro: O arquivo '{image_path}' não foi encontrado.")
    except Exception as e:
        print(f"Erro ao abrir a imagem: {e}")