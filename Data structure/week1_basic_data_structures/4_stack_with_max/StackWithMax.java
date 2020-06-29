import java.util.*;
import java.io.*;

public class StackWithMax {
    class FastScanner {
        StringTokenizer tok = new StringTokenizer("");
        BufferedReader in;

        FastScanner() {
            in = new BufferedReader(new InputStreamReader(System.in));
        }

        String next() throws IOException {
            while (!tok.hasMoreElements())
                tok = new StringTokenizer(in.readLine());
            return tok.nextToken();
        }

        int nextInt() throws IOException {
            return Integer.parseInt(next());
        }
    }

    public void solve() throws IOException {
        FastScanner scanner = new FastScanner();
        int queries = scanner.nextInt();
        Stack<Integer> stack = new Stack<Integer>();
        int maxEle = 0;

        for (int qi = 0; qi < queries; ++qi) {
            String operation = scanner.next();
            if ("push".equals(operation)) {
                int value = scanner.nextInt();

                if (stack.empty()) {
                    maxEle = value;
                    stack.push(value);
                }
                if (value > maxEle) {
                    stack.push(2 * value - maxEle);
                    maxEle = value;
                }

                else
                    stack.push(value);

            } else if ("pop".equals(operation)) {

                int t = stack.peek();
                stack.pop();

                if (t > maxEle)
                    maxEle = 2 * maxEle - t;

            } else if ("max".equals(operation)) {
                System.out.println(maxEle);
            }
        }
    }

    static public void main(String[] args) throws IOException {
        new StackWithMax().solve();
    }
}
