from src.services.authService import AuthService
from src.services.paragonService import ParagonService
if __name__ == "__main__":
    # Obtener el token desde AuthService (asumimos que ya lo tienes)
    
    auth_service = AuthService(user="dannyjacome", password="Gordito890081.")
    auth_service.login()  # Esto guarda user_id e id_token en la instancia
    iam_token = auth_service.id_token  # Usamos id_token como x-iam-token (ajusta según la API)

    topology_service = ParagonService(iam_token)
    topology_data = topology_service.get_topology()
    print("Topology data:", topology_data)