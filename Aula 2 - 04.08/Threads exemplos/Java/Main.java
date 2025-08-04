class MinhaThread extends Thread {
    public void run() {
        for (int i = 0; i<100; i++){
            System.out.println(i);
        }
    }
}

public class Main {
    public static void main(String[] args) {
        MinhaThread t = new MinhaThread();
        t.start();

        MinhaThread t2 = new MinhaThread();
        t2.start();

    }
}