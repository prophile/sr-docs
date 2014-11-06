---
layout: default
title: 2014 Competition Game Points
---
# Game Points Totals

This page shows the total number of game points scored by each team,
summed over all of their league matches.

For the current league points scores (including the league ranking),
see the [league points](/comp/league) page.
To see the details of the scores for each individual match, see the [points page](/comp/points).

<span data-ng-if="latest_match != null">
Up to date with scores from match {{latest_match}}.
</span>
<span data-ng-if="latest_match == null">
No scores have been recorded yet.
</span>

<!--- TODO:
* Add dynamic sorting rather than the fixed sorting by name?
-->

<table>
    <thead>
        <tr>
            <th>Team</th>
            <th>Points</th>
        </tr>
    </thead>
    <tr data-ng-repeat="item in game_points" id="{{item.tla}}">
        <td>
            <a href="/teams/{{item.tla}}" title="Find out more about team {{item.tla}}">{{item.tla}}</a>:
            {{item.tla|teamName:teams:true}}
        </td>
        <td>{{item.points}}</td>
    </tr>
</table>
