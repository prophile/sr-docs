---
layout: default
title: 2014 Match Points
---
<style type="text/css">
/* first column is more headers */
.scores .match:nth-child(2) { background-color: {{corners[0].colour|hexLighter:0.5}}; }
.scores .match:nth-child(3) { background-color: {{corners[1].colour|hexLighter:0.5}}; }
.scores .match:nth-child(4) { background-color: {{corners[2].colour|hexLighter:0.5}}; }
.scores .match:nth-child(5) { background-color: {{corners[3].colour|hexLighter:0.5}}; }
</style>

# Match Points

<div id="match-chooser">
    <!--- NB: local width style as otherwise Select2 doesn't get it right -->
    <select data-ng-model="$storage.chosenTeam"
            data-ui-select2
            style="width:350px;float:right;margin-right:7px;"
            >
        <option value="">Choose a team</option>
        <option data-ng-repeat="(tla, info) in teams"
                value="{{tla}}">
            {{tla|teamName:teams}}
        </option>
    </select>

    <p>
        Matches to show:
        <input data-ng-model="chosenMatches"
               data-ng-list
               data-placeholder="enter matches" />
    </p>
</div>

This page shows the league and game points earned during any match.
Either choose a team or enter a comma separated list of matches in the box to the right.

For a summary of all the teams' points, see either the [league](/comp/league) or [game points](/comp/gamepoints) pages.

<div class="points" data-ng-repeat="match in fetchedMatches|matchSort">
    <h4>Match {{match.num}}</h4>
    <div class="game"
         data-ng-repeat="(arena, game) in match.games">
        <h4>Arena {{arena}}</h4>
        <table class="scores" data-ng-if="game.scores">
            <thead>
                <tr>
                    <th></th>
                    <th data-ng-repeat="tla in game.teams"
                        data-ng-class="{match: tla==$storage.chosenTeam}">
                        {{tla}}
                    </th>
                </tr>
            </thead>
            <tr data-ng-repeat="(type, scores) in game.scores">
                <th>{{type|titleCase}}</th>
                <td data-ng-repeat="tla in game.teams"
                    data-ng-class="{match: tla==$storage.chosenTeam}">
                    {{scores[tla]}}
                </td>
            </tr>
        </table>
        <p data-ng-if="!game.scores">No scores yet recorded for this game.</p>
    </div>
</div>