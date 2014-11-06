---
layout: default
title: 2014 Competition League
---
# League Status

This page shows the current status of the league, with teams positioned by
the number of league points they have earned from their matches.
Ties are resolved by comparing the total number of [game points](/comp/gamepoints)
tied teams have earned in their league matches.

The positions of the teams within the league are used to seed the [knockouts](/comp/knockout).

Details of the scores for each individual match are available on the [points page](/comp/points).

<span data-ng-if="latest_match != null">
Up to date with scores from match {{latest_match}}.
</span>
<span data-ng-if="latest_match == null">
No scores have been recorded yet.
</span>

<table>
    <thead>
        <tr>
            <th>Position</th>
            <th>Points</th>
            <th>Team</th>
        </tr>
    </thead>
    <tr data-ng-repeat="item in league_points" id="{{item.tla}}">
        <td>{{item.pos}}</td>
        <td>{{item.points}}</td>
        <td>
            <a href="/teams/{{item.tla}}" title="Find out more about team {{item.tla}}">{{item.tla}}</a>:
            {{item.tla|teamName:teams:true}}
        </td>
    </tr>
</table>
