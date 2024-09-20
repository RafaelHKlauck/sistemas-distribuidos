import java.rmi.Remote;
import java.rmi.RemoteException;

public interface InterfaceRemota extends Remote {
  int sum(int primeiroNumero, int segundoNumero) throws RemoteException;
}