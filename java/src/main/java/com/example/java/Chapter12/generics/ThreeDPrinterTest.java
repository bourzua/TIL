package com.example.java.Chapter12.generics;

public class ThreeDPrinterTest {

    public static void main(String[] args) {

        ThreeDPrinter<Powder> printer = new ThreeDPrinter<Powder>();
        printer.setMaterial(new Powder());
        Powder powder = printer.getMaterial();
        System.out.println(printer);

        ThreeDPrinter<Plastic> printerPlastic = new ThreeDPrinter<Plastic>();
        printerPlastic.setMaterial(new Plastic());
        Plastic plastic = printerPlastic.getMaterial();
        System.out.println(printerPlastic);

//        ThreeDPrinter<Water> printerWater = new ThreeDPrinter<Water>();
//        printerWater.setMaterial(new Water());
//        System.out.println(printerWater);

        printerPlastic.printing();
    }
}
