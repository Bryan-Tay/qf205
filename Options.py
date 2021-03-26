<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Options</class>
 <widget class="QMainWindow" name="Options">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>782</width>
    <height>807</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="StockPrice">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>270</y>
      <width>104</width>
      <height>17</height>
     </rect>
    </property>
    <property name="text">
     <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:14pt; font-weight:600;&quot;&gt;Stock Price (S)&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
   </widget>
   <widget class="QLabel" name="Sigma">
    <property name="geometry">
     <rect>
      <x>210</x>
      <y>520</y>
      <width>68</width>
      <height>17</height>
     </rect>
    </property>
    <property name="text">
     <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:14pt; font-weight:600;&quot;&gt;Sigma (σ)&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
   </widget>
   <widget class="QLabel" name="Title">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>50</y>
      <width>351</width>
      <height>33</height>
     </rect>
    </property>
    <property name="text">
     <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;&lt;span style=&quot; font-size:28pt; font-weight:600; text-decoration: underline;&quot;&gt;Option Pricing Calculator&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
   </widget>
   <widget class="QLabel" name="YieldRate">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>420</y>
      <width>94</width>
      <height>17</height>
     </rect>
    </property>
    <property name="text">
     <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:14pt; font-weight:600;&quot;&gt;Yield Rate (q)&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
   </widget>
   <widget class="QLabel" name="MethodLine">
    <property name="geometry">
     <rect>
      <x>220</x>
      <y>220</y>
      <width>53</width>
      <height>17</height>
     </rect>
    </property>
    <property name="text">
     <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:14pt; font-weight:600;&quot;&gt;Method&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
   </widget>
   <widget class="QLabel" name="Periods">
    <property name="geometry">
     <rect>
      <x>130</x>
      <y>570</y>
      <width>148</width>
      <height>17</height>
     </rect>
    </property>
    <property name="text">
     <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:14pt; font-weight:600;&quot;&gt;No. of Time Steps (N)&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
   </widget>
   <widget class="QLabel" name="StrikePrice">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>320</y>
      <width>105</width>
      <height>17</height>
     </rect>
    </property>
    <property name="text">
     <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:14pt; font-weight:600;&quot;&gt;Strike Price (K)&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
   </widget>
   <widget class="QLabel" name="TimeEnd">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>470</y>
      <width>107</width>
      <height>17</height>
     </rect>
    </property>
    <property name="text">
     <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:14pt; font-weight:600;&quot;&gt;Time period (T)&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
   </widget>
   <widget class="QLabel" name="CallPrice">
    <property name="geometry">
     <rect>
      <x>190</x>
      <y>620</y>
      <width>86</width>
      <height>17</height>
     </rect>
    </property>
    <property name="text">
     <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:14pt; font-weight:600;&quot;&gt;Option Price&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
   </widget>
   <widget class="QLabel" name="TickerLabel">
    <property name="geometry">
     <rect>
      <x>220</x>
      <y>130</y>
      <width>44</width>
      <height>17</height>
     </rect>
    </property>
    <property name="text">
     <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:14pt; font-weight:600;&quot;&gt;Ticker&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
   </widget>
   <widget class="QLabel" name="Rate">
    <property name="geometry">
     <rect>
      <x>160</x>
      <y>370</y>
      <width>111</width>
      <height>17</height>
     </rect>
    </property>
    <property name="text">
     <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:14pt; font-weight:600;&quot;&gt;Interest Rate (r)&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="InputStepsN">
    <property name="geometry">
     <rect>
      <x>300</x>
      <y>570</y>
      <width>125</width>
      <height>21</height>
     </rect>
    </property>
   </widget>
   <widget class="QRadioButton" name="InputCallButton">
    <property name="geometry">
     <rect>
      <x>300</x>
      <y>620</y>
      <width>48</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>Call</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="InputStockPrice">
    <property name="geometry">
     <rect>
      <x>300</x>
      <y>270</y>
      <width>125</width>
      <height>21</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="InputTicker">
    <property name="geometry">
     <rect>
      <x>290</x>
      <y>130</y>
      <width>125</width>
      <height>21</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="InputYieldRate">
    <property name="geometry">
     <rect>
      <x>300</x>
      <y>420</y>
      <width>125</width>
      <height>21</height>
     </rect>
    </property>
   </widget>
   <widget class="QRadioButton" name="InputExplicitButton">
    <property name="geometry">
     <rect>
      <x>370</x>
      <y>220</y>
      <width>69</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>Explicit</string>
    </property>
   </widget>
   <widget class="QRadioButton" name="InputImplicitButton">
    <property name="geometry">
     <rect>
      <x>290</x>
      <y>220</y>
      <width>69</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>Implicit</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="InputSigma">
    <property name="geometry">
     <rect>
      <x>300</x>
      <y>520</y>
      <width>125</width>
      <height>21</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="InputTimePeriod">
    <property name="geometry">
     <rect>
      <x>300</x>
      <y>470</y>
      <width>125</width>
      <height>21</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="InputInterestRate">
    <property name="geometry">
     <rect>
      <x>300</x>
      <y>370</y>
      <width>125</width>
      <height>21</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="InputStrikePrice">
    <property name="geometry">
     <rect>
      <x>300</x>
      <y>320</y>
      <width>125</width>
      <height>21</height>
     </rect>
    </property>
   </widget>
   <widget class="QRadioButton" name="InputPutButton">
    <property name="geometry">
     <rect>
      <x>370</x>
      <y>620</y>
      <width>48</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>Put</string>
    </property>
   </widget>
   <widget class="QPushButton" name="InputCalculate">
    <property name="geometry">
     <rect>
      <x>280</x>
      <y>660</y>
      <width>113</width>
      <height>32</height>
     </rect>
    </property>
    <property name="text">
     <string>Calculate</string>
    </property>
   </widget>
   <widget class="QLabel" name="OutputText">
    <property name="geometry">
     <rect>
      <x>260</x>
      <y>700</y>
      <width>151</width>
      <height>41</height>
     </rect>
    </property>
    <property name="whatsThis">
     <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;&lt;br/&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
    <property name="text">
     <string>  </string>
    </property>
   </widget>
   <widget class="QPushButton" name="InputExtract">
    <property name="geometry">
     <rect>
      <x>290</x>
      <y>160</y>
      <width>113</width>
      <height>32</height>
     </rect>
    </property>
    <property name="text">
     <string>Extract Data</string>
    </property>
   </widget>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
