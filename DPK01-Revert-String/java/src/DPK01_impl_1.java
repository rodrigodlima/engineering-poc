public class DPK01_impl_1 {

    public static String reverseString(String str) {
        String reversed = "";

        for (int i = str.length() - 1; i >= 0; i--) {
            reversed += str.charAt(i);
        }

        return reversed;
    }

    public static void main(String[] args) {
        String original = "Hello";
        String reversed = reverseString(original);

        System.out.println(reversed);
    }
}