<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>782</width>
    <height>779</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="Periods">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>530</y>
      <width>251</width>
      <height>41</height>
     </rect>
    </property>
    <property name="text">
     <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:14pt; font-weight:600;&quot;&gt;No. of Time Steps (N)&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
   </widget>
   <widget class="QLabel" name="TimeEnd_2">
    <property name="geometry">
     <rect>
      <x>210</x>
      <y>440</y>
      <width>181</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:14pt; font-weight:600;&quot;&gt;Time period (T)&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
   </widget>
   <widget class="QLabel" name="Sigma_2">
    <property name="geometry">
     <rect>
      <x>250</x>
      <y>480</y>
      <width>121</width>
      <height>41</height>
     </rect>
    </property>
    <property name="text">
     <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:14pt; font-weight:600;&quot;&gt;Sigma (σ)&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
   </widget>
   <widget class="QLabel" name="Rate">
    <property name="geometry">
     <rect>
      <x>200</x>
      <y>330</y>
      <width>201</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:14pt; font-weight:600;&quot;&gt;Interest Rate (r)&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
   </widget>
   <widget class="QLabel" name="TickerLabel_2">
    <property name="geometry">
     <rect>
      <x>270</x>
      <y>130</y>
      <width>51</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:14pt; font-weight:600;&quot;&gt;Ticker&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
   </widget>
   <widget class="QLabel" name="Title_2">
    <property name="geometry">
     <rect>
      <x>110</x>
      <y>50</y>
      <width>601</width>
      <height>61</height>
     </rect>
    </property>
    <property name="text">
     <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;&lt;span style=&quot; font-size:28pt; font-weight:600; text-decoration: underline;&quot;&gt;Implicit Explicit Option Price Calculator&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="InputYieldRate">
    <property name="geometry">
     <rect>
      <x>360</x>
      <y>390</y>
      <width>125</width>
      <height>21</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="InputStrikePrice">
    <property name="geometry">
     <rect>
      <x>360</x>
      <y>290</y>
      <width>125</width>
      <height>21</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="InputSigma">
    <property name="geometry">
     <rect>
      <x>360</x>
      <y>490</y>
      <width>125</width>
      <height>21</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="InputStockPrice">
    <property name="geometry">
     <rect>
      <x>357</x>
      <y>240</y>
      <width>125</width>
      <height>21</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="InputTicker">
    <property name="geometry">
     <rect>
      <x>360</x>
      <y>130</y>
      <width>125</width>
      <height>21</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="MethodLine">
    <property name="geometry">
     <rect>
      <x>230</x>
      <y>200</y>
      <width>91</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:14pt; font-weight:600;&quot;&gt;Option Type&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
   </widget>
   <widget class="QLabel" name="OutputText">
    <property name="geometry">
     <rect>
      <x>340</x>
      <y>670</y>
      <width>171</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QPushButton" name="InputExtract">
    <property name="geometry">
     <rect>
      <x>360</x>
      <y>160</y>
      <width>117</width>
      <height>32</height>
     </rect>
    </property>
    <property name="text">
     <string>Extract Data</string>
    </property>
   </widget>
   <widget class="QPushButton" name="InputCalculate">
    <property name="geometry">
     <rect>
      <x>400</x>
      <y>630</y>
      <width>113</width>
      <height>32</height>
     </rect>
    </property>
    <property name="text">
     <string>Calculate</string>
    </property>
   </widget>
   <widget class="QLabel" name="StrikePrice_2">
    <property name="geometry">
     <rect>
      <x>210</x>
      <y>280</y>
      <width>181</width>
      <height>41</height>
     </rect>
    </property>
    <property name="text">
     <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:14pt; font-weight:600;&quot;&gt;Strike Price (K)&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
   </widget>
   <widget class="QLabel" name="YieldRate_2">
    <property name="geometry">
     <rect>
      <x>220</x>
      <y>380</y>
      <width>171</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:14pt; font-weight:600;&quot;&gt;Yield Rate (q)&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
   </widget>
   <widget class="QLabel" name="StockPrice_2">
    <property name="geometry">
     <rect>
      <x>210</x>
      <y>240</y>
      <width>181</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:14pt; font-weight:600;&quot;&gt;Stock Price (S)&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="InputInterestRate">
    <property name="geometry">
     <rect>
      <x>360</x>
      <y>340</y>
      <width>125</width>
      <height>21</height>
     </rect>
    </property>
   </widget>
   <widget class="QRadioButton" name="InputPutButton">
    <property name="geometry">
     <rect>
      <x>440</x>
      <y>200</y>
      <width>48</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>Put</string>
    </property>
   </widget>
   <widget class="QRadioButton" name="InputCallButton">
    <property name="geometry">
     <rect>
      <x>360</x>
      <y>200</y>
      <width>48</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>Call</string>
    </property>
   </widget>
   <widget class="QLabel" name="CallPrice">
    <property name="geometry">
     <rect>
      <x>210</x>
      <y>670</y>
      <width>151</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:14pt; font-weight:600;&quot;&gt;Option Price&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="InputTimePeriod">
    <property name="geometry">
     <rect>
      <x>360</x>
      <y>440</y>
      <width>125</width>
      <height>21</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="InputReset">
    <property name="geometry">
     <rect>
      <x>280</x>
      <y>630</y>
      <width>113</width>
      <height>32</height>
     </rect>
    </property>
    <property name="text">
     <string>Reset</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="InputStepsN">
    <property name="geometry">
     <rect>
      <x>360</x>
      <y>540</y>
      <width>125</width>
      <height>21</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="InputStepsM">
    <property name="geometry">
     <rect>
      <x>360</x>
      <y>590</y>
      <width>125</width>
      <height>21</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="Periods_2">
    <property name="geometry">
     <rect>
      <x>290</x>
      <y>580</y>
      <width>31</width>
      <height>41</height>
     </rect>
    </property>
    <property name="text">
     <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:14pt; font-weight:600;&quot;&gt;(M)&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
   </widget>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
