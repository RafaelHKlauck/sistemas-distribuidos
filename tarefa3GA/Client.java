import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.Random;

public class Client implements Runnable {
  private final InterfaceRemota stub;

  public Client(InterfaceRemota stub) {
    this.stub = stub;
  }

  @Override
  public void run() {
    Random random = new Random();
    try {
      for (int i = 0; i < 5; i++) {
        int num1 = random.nextInt(101);
        int num2 = random.nextInt(101);
        int response = stub.sum(num1, num2);
        System.out.println(Thread.currentThread().getName() + " - Request: " + num1 + " + " + num2 + " = " + response);
      }
    } catch (Exception e) {
      e.printStackTrace();
    }
  }

  public static void main(String[] args) {
    try {
      Registry registry = LocateRegistry.getRegistry("localhost", 6006);
      InterfaceRemota stub = (InterfaceRemota) registry.lookup("sum");

      // Criação de múltiplos clientes
      for (int i = 0; i < 5; i++) {
        new Thread(new Client(stub), "Client-" + i).start();
      }
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}