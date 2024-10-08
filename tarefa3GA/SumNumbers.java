import java.rmi.server.UnicastRemoteObject;
import java.rmi.RemoteException;

public class SumNumbers extends UnicastRemoteObject implements InterfaceRemota {
  public SumNumbers() throws RemoteException {
    super();
  }

  int lastSumResult = 0;

  @Override
  public synchronized int sum(int primeiroNumero, int segundoNumero) throws RemoteException {
    System.out.println(Thread.currentThread().getName() + " - Entrando no método sum");
    try {
      // Simulando um processamento mais longo
      Thread.sleep(1000);
    } catch (InterruptedException e) {
      Thread.currentThread().interrupt();
    }

    int soma = primeiroNumero + segundoNumero;
    lastSumResult = soma;
    System.out.println(Thread.currentThread().getName() + " - Saindo do método sum com resultado: " + soma);
    return soma;
  }

  @Override
  public int getLastSumResult() throws RemoteException {
    return lastSumResult;
  }

}
