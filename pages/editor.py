import sqlite3
import streamlit as st
from streamlit.runtime.scriptrunner.script_run_context import get_script_run_ctx as get_report_ctx
import warnings

conn = sqlite3.connect("bd/bd.sqlite3")
cursor = conn.cursor()


def main():
    conn = st.experimental_connection("local_db",
                                      type="sql",
                                      url="sqlite:///bd/bd.sqlite3"
                                      )
    df = conn.query("select * from products")
    st.data_editor(df, key="data_editor", num_rows="dynamic")
    st.write("Here's the session state:")
    st.write(st.session_state["data_editor"])
    update_price = st.session_state["data_editor"]

    get_price_WB = st.button('Сохранить цены')
    if get_price_WB:
        js_price(update_price)
        st.experimental_rerun()






    # response = st.session_state["data_editor1"]
    # conn = sqlite3.connect('bd/bd.sqlite3')
    # cursor = conn.cursor()
    # print(response)
    # print(response['edited_rows'])
    # print(response['edited_rows'][1])
    # print(response['edited_rows'][1]['discount'])

    # for item in response:
    #     price = item['price']
    #     nmID = item['nmId']
    #     discount = item['discount']
        # cursor.execute(f"UPDATE products SET price = {price}, discount = {discount} WHERE id_wb = {nmID}")


def js_price(date):
    for key in date['edited_rows']:
        pk = key + 1
        price = date['edited_rows'][key]['price']
        cursor.execute(f"UPDATE products SET price = {price} WHERE pk = {pk}")
        conn.commit()
        conn.close()

        print(id, price)



if __name__ == '__main__':
    main()
