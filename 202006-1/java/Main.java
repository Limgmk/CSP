import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * @time 2020/8/13 下午12:22
 * @author Limgmk
 * @description
 */
public class Main {
    public static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        List<Info> infoList = new ArrayList<Info>();
        List<Line> lineList = new ArrayList<Line>();

        int num1 = sc.nextInt();
        int num2 = sc.nextInt();

        for(int i = 0; i < num1; i++) {
            Info info = new Info(sc.nextInt(), sc.nextInt(), sc.next());
            infoList.add(info);
        }

        for(int i = 0; i < num2; i++) {
            Line line = new Line(sc.nextInt(), sc.nextInt(), sc.nextInt());
            lineList.add(line);
        }

        for(Line line: lineList) {
            String ok = "Yes";
            Info firstInfo = infoList.get(0);
            int resultFirst = line.a + line.b * firstInfo.x + line.c * firstInfo.y;
            String infoType = "";
            if(resultFirst == 0) {
                ok = "No";
            } else {
                if ((resultFirst > 0 && firstInfo.type.equals("A")) || (resultFirst < 0 && !firstInfo.type.equals("A"))) {
                    infoType = "A";
                } else {
                    infoType = "B";
                }
                for(Info info: infoList) {
                    int result = line.a + line.b * info.x + line.c * info.y;
                    if(result == 0 || (result > 0 && !info.type.equals(infoType)) || (result < 0 && info.type.equals(infoType))) {
                        ok = "No";
                        break;
                    }
                }
            }

            System.out.println(ok);
        }
    }

    static class Info {
        public int x;
        public int y;
        public String type;

        public Info(int x, int y, String type) {
            this.x = x;
            this.y = y;
            this.type = type;
        }
    }

    static class Line {
        public int a;
        public int b;
        public int c;

        public Line(int a, int b, int c) {
            this.a = a;
            this.b = b;
            this.c = c;
        }
    }
}
