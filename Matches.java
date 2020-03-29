import java.io.BufferedReader;
import java.io.InputStreamReader;
public class Main {
	public static boolean func(long n , long m , boolean ans) {		
		//System.out.println(ans + " " + n + " " + m);
		if (n==0 || m==0 || n==m || n%m == 0) {
			return ans ;
		}
		else {
			if (n/m >1 || m/n >1) {
				return ans;
			}
			else {
				if (n>m) {
					n = n-m;
				}
				else if (m>n) {
					m = m-n ;
				}
				ans = !ans;
				return func(n,m,ans);
			}
		}
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try{
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			int t = Integer.parseInt(br.readLine());
			for (int p= 0; p< t ; p++) {
				String[] inp = br.readLine().trim().split("\\s+");
			    long n = Long.parseLong(inp[0]);
			    long m = Long.parseLong(inp[1]);
			    
			    
				boolean ans = true;		    
			    ans = func(n,m,ans);
			    if (ans == true) {
			    	System.out.println("Ari");
			    }
			    if (ans==false) {
			    	System.out.println("Rich");
			    }
			}
			
			
		}
		catch (Exception E) {}
				
	}

}
