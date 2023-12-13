package base;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import provider.fligt_list_view;
import provider.homepage;
import provider.seat_view;
import provider.profile.user_details;
import provider.sales_report.sales_report_day;


public class headbar{
    static JButton home;
    static JButton sr;
    static JButton lf;
    static JButton sv;
    static JButton profile;
    static JFrame frame = homepage.frame;
    static String cmp_name = homepage.company_name;
    public static JPanel starter(JPanel panel){

        
        buttons(panel);
        listeners(panel);
        panel.add(new JSeparator());
        panel.setBackground(Color.WHITE);
        return panel;
    }

    static JPanel buttons(JPanel panel){
            Color clr = Color.decode("#828282");
            JMenuBar jmb = new JMenuBar();
            home = new JButton("TIGERFIRE JET");
            sr = new JButton("Sales Report");
            lf = new JButton("List Flights");
            sv = new JButton("Seat View");
            profile  = new JButton("Profile");

            home.setBackground(clr);
            sr.setBackground(clr);
            lf.setBackground(clr);
            sv.setBackground(clr);
            profile.setBackground(clr);
            jmb.add(home);
            jmb.add(new JSeparator());
            jmb.add(sr);
            jmb.add(lf);
            jmb.add(sv);
            jmb.add(profile);

            jmb.setBounds(0, 0, 700, 30);
            panel.add(jmb);
            panel.setLayout(null);
            return panel;
    }

    static void listeners(JPanel panel){
        home.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent ae){
                panel.removeAll();
                homepage.home_page(frame,cmp_name);
            }
        });
        profile.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent ae){
                panel.removeAll();
                user_details.details_user(frame,cmp_name);
            }
        });
        sr.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent ae){
                panel.removeAll();
                sales_report_day.report_day(frame, cmp_name);
            }
        });
        lf.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent ae){
                panel.removeAll();
                fligt_list_view.flight_list(frame);
            }
        });
        sv.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent ae){
                panel.removeAll();
                seat_view.view_seat(frame);
            }
        });
    }
}