#!/usr/bin/env python
# coding=utf-8
# author: J3n5en@WangYuan
from flask import Flask,jsonify
from helper.CetTicket import CetTicket
from werkzeug.contrib.fixers import ProxyFix 
app = Flask(__name__)


@app.route('/GetCetScore/<ticket>/<username>',methods=['POST','GET'])
def get_cet_score(ticket, username):
    ct = CetTicket()
    try:
        result = ct.get_score(ticket, username)
        result['ticket'] = ticket
    except:
        result = {'Status': '0', 'Contact_us': 'wangyuan.info'}
    return jsonify(result)


@app.route('/GetCetScoreWithoutTickets/<province>/<school>/<cet_type>/<username>',methods=['POST','GET'])
def get_cet_score_without_tickets(province, school,cet_type,username):
    ct = CetTicket()
    try:
        ticket = ct.find_ticket_number(province, school, username, cet_type=int(cet_type))
        result = ct.get_score(ticket, username)
        result['ticket'] = ticket
    except:
        result = {'Status': '0', 'Contact_us': 'wangyuan.info'}
    return jsonify(result)


@app.route('/GetCetScoreWithoutTicketsForWechat/<cet_type>/<username>',methods=['POST','GET'])
def friend_cet(cet_type,username):
    ct = CetTicket()
    try:
        ticket = ct.find_ticket_number("广东".decode("utf-8"), "韶关学院".decode("utf-8"), username, cet_type=int(cet_type))
        result = ct.get_score(ticket, username)
        result['ticket'] = ticket
    except:
        result = {'Status': '0', 'Contact_us': 'wangyuan.info'}
    return jsonify(result)

app.wsgi_app = ProxyFix(app.wsgi_app) 
if __name__ == '__main__':
    app.run()