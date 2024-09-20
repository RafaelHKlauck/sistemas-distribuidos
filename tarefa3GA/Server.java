import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class Server {
  public static void main(String args[]) {
    try {
      SumNumbers obj = new SumNumbers();
      Registry registry = LocateRegistry.createRegistry(6006);
      registry.rebind("sum", obj);
      System.out.println("Server ready");
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}