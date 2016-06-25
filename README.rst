===================
Scrapping rutracker
===================

Here lies weak rutracker parser.

Code is kind a stinky, but might be usefull.

Also scrappy spider is included.

.. 
   To destroy community, one must give em right to rule.

Login
-----

POST request should be sent to `url <http://rutracker.org/forum/login.php>`_

.. code-block::

   <form id="login-form-quick" method="post" action="login.php" style="display: inline;">
       <input 
           id="top-login-uname" 
           type="text" 
           name="login_username" 
           tabindex="1"
           accesskey="l"
           placeholder="имя">
       <input 
           id="top-login-pwd" 
           type="password" 
           name="login_password" tabindex="2" 
           placeholder="пароль">
       <label title="Защищенное соединение">
           <input 
               class="login-ssl" 
               type="checkbox" 
               tabindex="3">SSL
       </label>
       <input 
           id="top-login-btn" 
           type="submit"
           name="login" 
           value="вход" 
           tabindex="4">
   </form>

SEARCH
------

.. code-block::

   <form id="quick-search" method="post" action="#">
       <input 
           type="hidden" 
           name="max" 
           value="1">
       <input 
           id="search-text" 
           type="text" name="nm" 
           value="" 
           tabindex="1" 
           accesskey="q">
       <select 
           id="search-menu" 
           tabindex="2">
           <option value="search-tr" data-action="tracker.php" selected="">
               &nbsp;раздачи&nbsp;
           </option>
           <option value="search-all" data-action="search.php">
               &nbsp;все темы&nbsp;
           </option>
           <option value="cse">&nbsp;в google&nbsp;</option>
           <option value="wiki">&nbsp;в wiki </option>
           <option value="hash">&nbsp;по info_hash </option>
       </select>
       <input
           id="search-submit" 
           type="submit" 
           value="поиск" 
           tabindex="3">
   </form>

Results parsing
---------------


.. code-block::

   //*[@id="tor-tbl"]/tbody/tr[1]/td[4]/div[1]/a
