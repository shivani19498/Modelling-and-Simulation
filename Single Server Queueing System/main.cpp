#include<bits/stdc++.h>
#include<conio.h>
using namespace std;

void waiting_time(int n, int bt[], int wt[], int at[])
{
	int service_time[n];
	service_time[0]=0;
	wt[0]=0;

for (int i = 1; i < n ; i++)
    {
        service_time[i] = service_time[i-1] + bt[i-1];
        wt[i] = service_time[i] - at[i];

        if (wt[i] < 0)
            wt[i] = 0;
    }
}

void turn_around_time(int n, int bt[],
                                      int wt[], int tat[])
{
    for (int i = 0; i < n ; i++)
        tat[i] = bt[i] + wt[i];
}

void avg_time(int p[], int n, int bt[], int at[])
{
    int wt[n], tat[n];

    waiting_time(n, bt, wt, at);

    turn_around_time(n, bt, wt, tat);

    cout << "id " << " Service Time " << " Arrival Time "
         << " Waiting Time " << " Completion Time \n";
    int total_wt = 0, total_tat = 0;
    for (int i = 0 ; i < n ; i++)
    {
        total_wt = total_wt + wt[i];
        total_tat = total_tat + tat[i];
        int compl_time = tat[i] + at[i];
        cout << " " << i+1 << "\t\t" << bt[i] << "\t\t"<< at[i] << "\t\t" << wt[i] << "\t\t "<< compl_time << endl;
    }

    cout << "Average waiting time = "<< (float)total_wt / (float)n;

}

int main()
{
    int p[] = {1, 2, 3};
    int n = sizeof p / sizeof p[0];

    int burst_time[] = {4, 6, 6};

    int arrival_time[] = {0, 2, 4};

    avg_time(p, n, burst_time, arrival_time);
    getch();
    return 0;
}
