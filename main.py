import generate_qr
import time
from utils import limpar_tela

def generate_menu():
    print("===================================")
    print("         QR Code Generator          ")
    print("        CLI QRCode Generator        ")
    print("    By: Dave G. Farias (o brabo)    ")
    print("===================================")
    print()

def main():
    while True:
        limpar_tela()
        generate_menu()

        url = input("🔗 Digite a URL ou texto para gerar o QR Code: ").strip()

        if not url:
            print("\n⚠️  Por favor, insira algum texto ou URL!")
            time.sleep(1.5)
            continue

        print("\n⏳ Gerando QR Code...")
        generate_qr.generator(url)
        print("✅ QR Code gerado com sucesso!\n")

        while True:
            print("Deseja criar outro QR Code?")
            print("  [1] Sim")
            print("  [2] Não (sair)")
            choice = input("➡️  Escolha uma opção: ").strip()

            if choice == "1":
                print("\n🔄 Voltando ao menu...\n")
                time.sleep(1.5)
                break
            elif choice == "2":
                print("\n👋 Obrigado por usar o QR Code Generator!")
                time.sleep(1.5)
                limpar_tela()
                exit()
            else:
                print("\n⚠️  Opção inválida! Tente novamente.\n")
                time.sleep(1.2)


if __name__ == "__main__":
    main()
